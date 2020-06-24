# Copyright (c) 2000-2012, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Name:           jsap
Version:        2.1
Release:        14.3%{?dist}
Summary:        A Java-based Simple Argument Parser
License:        LGPLv3+
Source0:        http://prdownloads.sourceforge.net/jsap/JSAP-2.1-src.tar.gz
Source1:        http://central.maven.org/maven2/com/martiansoftware/jsap/2.1/jsap-2.1.pom
Patch0:         jsap-javadoc.patch
Patch1:         jsap-javac.patch
URL:            http://www.martiansoftware.com/jsap/
BuildArch:      noarch

BuildRequires:  javapackages-local
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  xstream
BuildRequires:  rundoc
BuildRequires:  snip
BuildRequires:  xmlto

# /usr/share/maven-metadata needs an owner:
Requires:       javapackages-tools

%description 
JSAP not only syntactically validates your program's command line
arguments, but it converts those arguments into objects you specify. If you
tell JSAP that one of your parameters is an Integer, for example, and the
user does not provide a String that can be converted to an Integer when
invoking the program, JSAP will throw a ParseException when you have it
parse the command line. If no exception is thrown, you are guaranteed an
Integer when you request that parameter's value from your program. There's
a pretty big (and growing) list of return types supported by JSAP, including
Integers, Floats, Dates, URLs, and even java.awt.Colors; you can also add
your own in a matter of minutes.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%package doc
Summary:        Manual for %{name}

%description doc
Manual for %{name}.

%prep
%setup -q -c

rm JSAP-%{version}/lib/ant.jar
rm JSAP-%{version}/lib/JSAP-2.1.jar
rm JSAP-%{version}/lib/junit.jar
rm JSAP-%{version}/lib/rundoc-0.11.jar
rm JSAP-%{version}/lib/snip-0.11.jar
rm JSAP-%{version}/lib/xstream-1.1.2.jar

%patch0 
%patch1 

cp %{SOURCE1} %{name}.pom

%build
mv JSAP-%{version}/* .
export CLASSPATH=%(build-classpath xstream snip rundoc junit)
ant \
  -Dversion=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  -Dxstream.apiurl=%{_javadocdir}/xstream/core \
  jar javadoc manual
mv doc/javadoc .

# Tell XMvn which artifact belongs to which POM
%mvn_artifact %{name}.pom dist/JSAP-%{version}.jar


%install
%mvn_install -J javadoc/


%files -f .mfiles
%doc LICENSE.TXT CHANGELOG.TXT
%dir %{_datadir}/maven-poms/%{name}/
%dir %{_javadir}/%{name}/

%files javadoc -f .mfiles-javadoc
%doc LICENSE.TXT

%files doc
%doc doc/*
%doc LICENSE.TXT

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-14.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-13.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 20 2014 Ismael Olea <ismael@olea.org> - 2.1-5.3
- More review suggestions from https://bugzilla.redhat.com/show_bug.cgi?id=1127894

* Sat Aug  16 2014 Ismael Olea <ismael@olea.org> - 2.1-5.2
- Spec enhancenments

* Thu Aug  7 2014 Ismael Olea <ismael@olea.org> - 2.1-5.1
- Fedora build

* Thu Nov 01 2012 Will Tatam <will.tatam@red61.com> 2.1-5
- Auto rebuild for JPackage 6 in centos5 mock

* Mon Aug 13 2012 Ralph Apel <r.apel@r-apel.de> 0:2.1-4
- First JPP-6 release

* Wed Jan 14 2009 Sebastiano Vigna <vigna@acm.org> 0:2.1-3.jpp5
- Fixed spec file

* Fri Dec 26 2008 Sebastiano Vigna <vigna@acm.org> 0:2.1-1jpp
- Updated to 2.1

* Tue Jun 21 2005 Sebastiano Vigna <vigna@acm.org> 0:2.0-1jpp
- Updated to 2.0--many new features

* Wed Mar 16 2005 Sebastiano Vigna <vigna@acm.org> 0:1.03a-1jpp
- First JPackage version
