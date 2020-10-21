Name:           plexus-interactivity
Summary:        Plexus Interactivity Handler Component
Epoch:          0
Version:        1.0
Release:        4%{?dist}
License:        MIT

URL:            https://github.com/codehaus-plexus/plexus-interactivity
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
Source1:        LICENSE.MIT

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jline:jline) >= 2
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.


%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.


%package api
Summary:        API for %{name}

%description api
API module for %{name}.


%package jline
Summary:        jline module for %{name}

%description jline
jline module for %{name}.


%prep
%autosetup -n %{name}-%{name}-%{version} -p1

cp %{SOURCE1} .

# use jline2, not jline1
%pom_change_dep jline:jline jline:jline:2.10 plexus-interactivity-jline
sed -i "s!jline.ConsoleReader!jline.console.ConsoleReader!" \
    plexus-interactivity-jline/src/main/java/org/codehaus/plexus/components/interactivity/jline/JLineInputHandler.java

%pom_remove_plugin :maven-site-plugin

%mvn_file ":{plexus}-{*}" @1/@2

%mvn_package ":plexus-interactivity"


%build
%mvn_build -s


%install
%mvn_install


%files -f .mfiles
%license LICENSE.MIT

%files api -f .mfiles-plexus-interactivity-api
%license LICENSE.MIT

%files jline -f .mfiles-plexus-interactivity-jline
%license LICENSE.MIT

%files javadoc -f .mfiles-javadoc
%license LICENSE.MIT


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0:1.0-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Fabio Valentini <decathorpe@gmail.com> - 0:1.0-1
- Update to version 1.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-0.29.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-0.28.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Michael Simacek <msimacek@redhat.com> - 0:1.0-0.27.alpha6
- Include license file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-0.26.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-0.25.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-0.24.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-0.23.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-0.22.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.21.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.20.alpha6
- Update upstream URL

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.19.alpha6
- Rebuild to fix Maven auto-requires

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.18.alpha6
- Rebuild to fix requires and provides

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.17.alpha6
- Fix build-requires on plexus-components-pom

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.16.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.0-0.15.alpha6
- Use Requires: java-headless rebuild (#1067528)

* Fri Feb 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.14.alpha6
- Remove requires on subpackages from main package

* Fri Feb 21 2014 Michael Simacek <msimacek@redhat.com> - 0:1.0-0.13.alpha6
- Split into subpackages

* Tue Oct 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.12.alpha6
- Build with XMvn
- Remove %%pre javadoc scriplet
- Port to jline2, resolves: rhbz#1022978

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.11.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.10.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:1.0-0.9.alpha6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Dec 11 2012 Michal Srb <msrb@redhat.com> - 0:1.0-0.8.alpha6
- Removed dependency on plexus-container-default (Resolves: #878573)
- Fixed rpmlint warning

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.7.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  2 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.0-0.6.alpha6
- Add patch to fix build issues

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.5.a6.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.4.a6.8
- Build with maven 3.
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.4.a6.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  1 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.0-0.3.a6.7
- Fix pom filenames (Resolves rhbz#655821)
- Cleanups according to new guidelines

* Wed Oct 6 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.3.a6.6
- Use javadoc:aggregate.

* Wed Jul 21 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.3.a6.5
- Really fix depmaps.

* Wed Jul 21 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.3.a6.4
- Add parent/subname defines to fix poms/depmaps.

* Wed Jul 21 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.3.a6.3
- Update to alpha 6.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.3.a5.2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.2.a5.2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-0.1.a5.2.3
- drop repotag
- fix license tag

* Tue Mar 13 2007 Matt Wringe <mwringe@redhat.com> 1.0-0.1.a5.2jpp.2
- Add missing build requires for ant-nodeps

* Fri Feb 16 2007 Andrew Overholt <overholt@redhat.com> 1.0-0.1.a5.2jpp.1
- Remove javadoc symlinking

* Thu Feb 23 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.0-0.a5.2jpp
- First JPP 1.7 build
- With remavenization to 1.1 by Deepak Bhole <dbhole@redhat.com>

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.a5.1jpp
- First JPackage build
