FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt /root/
RUN pip install -r /root/requirements.txt

COPY *.py ${LAMBDA_TASK_ROOT}

CMD ["lambda_function.lambda_handler"]