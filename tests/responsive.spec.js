const {test,expect}=require('@playwright/test');
for(const width of [320,360,390,430,768,1024,1280,1440,1920])test(`no horizontal overflow at ${width}px`,async({page})=>{await page.setViewportSize({width,height:900});await page.goto('/');const overflow=await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);expect(overflow).toBeLessThanOrEqual(1)});
