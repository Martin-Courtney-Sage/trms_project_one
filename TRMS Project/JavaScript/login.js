
async function checkCred(){
    console.log("Authorizing....")
    const httpResponse = await fetch("#")
    console.log(httpResponse)
    const body = httpResponse.json()
    console.log(body)
}