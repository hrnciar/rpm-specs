Name:     yydebug
Version:  1.1.0
Release:  22%{?dist}
Summary:  Supports tracing and animation for a Java-based parser generated by jay
License:  BSD
URL:      http://www.cs.rit.edu/~ats/projects/lp/doc/jay/yydebug/package-summary.html
Source0:  http://www.cs.rit.edu/~ats/projects/lp/doc/jay/yydebug/doc-files/src.jar
Source1:  http://repo1.maven.org/maven2/org/jruby/jay-yydebug/1.0/jay-yydebug-1.0.pom

BuildRequires: maven-local
BuildRequires: sonatype-oss-parent

BuildArch:      noarch

%description
jay/yydebug supports tracing and animation for a Java-based parser generated 
by jay. An implementation of yyDebug is passed as an additional argument to 
yyparse() to trace a Java-based parser generated by jay with option -t set.
yyDebugAdapter produces one-line messages, by default to standard output. 
The messages are designed to be filtered by a program such as grep. yyAnim 
provides an animation of the parsing process

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jay-yydebug -c %{name}-%{version}

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

cp %{SOURCE1} pom.xml

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc jay/yydebug/package.html

%files javadoc -f .mfiles-javadoc


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 21 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.0-16
- rebuilt to fix FTBFS rhbz #1424567

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 16 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1.0-11
- Mavenize yydebug (#1019877)
- Cleanup unneeded parts, update to latest guidelines

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May  06 2010  Mohammed Morsi <mmorsi@redhat.com> - 1.1.0-5
- added my name which was missing in this changelog

* Wed May  05 2010  Mohammed Morsi <mmorsi@redhat.com> - 1.1.0-4
- added Alexander Kurtakov's patch to generate javadocs
- added javadoc bits to the spec

* Tue May  04 2010  Mohammed Morsi <mmorsi@redhat.com> - 1.1.0-3
- BSD license retrieved from 'jay' superproject
- http://svn.codehaus.org/jruby/trunk/jay/jay.1

* Tue Apr  27 2010  Mohammed Morsi <mmorsi@redhat.com> - 1.1.0-2
- removed gcj bits

* Wed Jan  21 2009  Mohammed Morsi <mmorsi@redhat.com> - 1.1.0-1
- Initial build.
