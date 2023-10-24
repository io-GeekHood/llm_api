from typing import Union
import os
from fastapi import FastAPI, Request, Response, status
from fastapi_utils.inferring_router import InferringRouter
from llm_api.util.dto import Query,Result
from llm_api.util.logging import getLogger
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

logger = getLogger(__name__)

# inititate application requirements
app = FastAPI()
router = InferringRouter() 

path = "models/Open-Orca/Mistral-7B-OpenOrca"

device = "cuda:0"
MISTRALMODEL = AutoModelForCausalLM.from_pretrained(path,torch_dtype=torch.float16).to(device)
MISTRALTOKENIZER = AutoTokenizer.from_pretrained(path)


@app.get("/query")
@torch.cuda.amp.autocast()
@torch.no_grad()
@torch.inference_mode()
async def operator(ingres:Query,response:Response):
    logger.info(f"proccessing new prompt {ingres.query}",extra={"scope":"server"})
    try:
        global MISTRALMODEL,MISTRALTOKENIZER
        model_inputs = MISTRALTOKENIZER([ingres.query], return_tensors="pt").to(device)
        generated_ids = MISTRALMODEL.generate(**model_inputs,max_length=80, max_new_tokens=80, do_sample=True)
        result = MISTRALTOKENIZER.batch_decode(generated_ids,skip_special_tokens=True)[0]
        return {"success":True,"exception": "","result":[str(result)]}
    except Exception as e:
        logger.exception('Something went wrong while vectorizing data.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"success":False,"exception": f"generation proccess failiure {e}","result":[]}


app.include_router(router)
