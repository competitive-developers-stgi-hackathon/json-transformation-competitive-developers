package com.bazaarvoice.jolt.sample;
import com.bazaarvoice.jolt.Chainr;
import com.bazaarvoice.jolt.JsonUtils;

import java.io.IOException;
import java.util.List;
public class JoltSample {

	public static void main(String[] args) throws IOException {
		List chainrSpecJSON = JsonUtils.classpathToList( "/jsonfiles/spec.json" );
	
        Chainr chainr = Chainr.fromSpec( chainrSpecJSON );

        Object inputJSON = JsonUtils.classpathToObject( "/jsonfiles/input.json" );

        Object transformedOutput = chainr.transform( inputJSON );

        System.out.println( JsonUtils.toJsonString( transformedOutput ) );
	}

}
