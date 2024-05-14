import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
from main import segment_everything
import io
from starlette.responses import StreamingResponse

app = FastAPI()

@app.post("/segment-image")
async def segment_image(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file).convert("RGB")
        result_image = segment_everything(image=image)
        # Convert PIL image to bytes
        img_byte_array = io.BytesIO()
        # Save the segmented image into the byte stream in PNG format
        result_image.save(img_byte_array, format='PNG')
        img_byte_array.seek(0)
        return StreamingResponse(content=img_byte_array, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
