$hookurl = "https://discord.com/api/webhooks/994626188238672023/7zw_uIhUGlxwW09osLnHcMtSqFy5S1ZYzDEJJXGSkeCIyRCLzChTpC03A9U7ZtbSSkRe"
$content = @"
Yo it's time to game
"@
$payload = [PSCustomObject]@{
    content = $content
}
Invoke-RestMethod -Uri $hookurl -method post -Body ($payload | ConvertTo-Json) -ContentType 'application/json'