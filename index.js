import puppeteer from "puppeteer-core";

async function run(){
  let browser;
  try{
    browser = await puppeteer.connect({

      browserWSEndpoint: `wss://`
    })

    return
  }
  catch(e){
    console.error('scrape failed', e)
  }
  finally{
    await browser?.close()
    
  }
}
