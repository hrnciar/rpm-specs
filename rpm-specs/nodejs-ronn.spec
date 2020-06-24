%{?nodejs_find_provides_and_requires}

Name:       nodejs-ronn
Version:    0.4.0
Release:    16%{?dist}
Summary:    Markdown to roff/html converter
License:    MIT
URL:        https://github.com/kapouer/ronnjs
Source0:    https://registry.npmjs.org/ronn/-/ronn-%{version}.tgz
Patch0:	    puts.patch

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
JavaScript port of ronn, using markdown-js to produce roff man pages. Not fully
compatible with ronn, although it aims to be, wherever possible.

%prep
%setup -q -n package
%patch0 -p3 -b .puts

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/ronn
cp -pr bin lib package.json %{buildroot}%{nodejs_sitelib}/ronn

mkdir -p %{buildroot}%{_bindir}
ln -s ../lib/node_modules/ronn/bin/ronn.js %{buildroot}%{_bindir}/ronn-nodejs

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/ronn
%{_bindir}/ronn-nodejs
%doc README.md CHANGES TODO
%license LICENSE

%changelog
* Wed May 20 2020 Stuart Gathman <stuart@gathman.org> - 0.4.0-16
- Patch obsolete puts calls to use console

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.4.0-8
- cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.0-4
- add macro to invoke dependency generator on EL6

* Sun Jul 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-3
- restrict to compatible arches

* Wed Jun 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.0-2
- rename executable so as not to conflict with rubygem-ronn

* Tue Apr 16 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.0-1
- new upstream release 0.4.0
- markdown now unbundled upstream

* Wed Mar 20 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.8-6
- fix require on markdown

* Sat Mar 16 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.8-5
- unbundle markdown

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.8-4
- add missing build section
- capitalize summary

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.8-3
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.8-2
- guard Requires for F17 automatic depedency generation

* Sat Feb 25 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.8-1
- new upstream release 0.3.8

* Sun Dec 18 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.7-2
- add Group to make EL5 happy

* Thu Nov 17 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.7-1
- initial package
