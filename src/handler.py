""" Example handler file. """

import runpod

# If your handler runs inference on a model, load the model here.
# You will want models to be loaded into memory before starting serverless.


def handler(job):
    """ Handler function that will be used to process jobs. """
    job_input = job['input']

    dance_id = job_input.get('dance_id')
    img_url = job_input.get('img_url')

    // prepare dance vidoe 

    // download image

    // process inference
    copy-paste

    process_id = subProcess(f'python3.11 inference.py ..{param1}.{param1}.{param1}.'

    judge process_id
    // upload generated video (firebase)

    // get uploaded video url

    return {url: url}


runpod.serverless.start({"handler": handler})
