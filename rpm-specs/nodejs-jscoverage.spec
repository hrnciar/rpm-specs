%{?nodejs_find_provides_and_requires}

# Not all dependencies have been satisfied yet.
%global enable_tests 0

Name:       nodejs-jscoverage
Version:    0.3.8
Release:    12%{?dist}
Summary:    A JavaScript coverage tool for Node.js and browser development
License:    MIT
URL:        https://github.com/fishbar/jscoverage
Source0:    http://registry.npmjs.org/jscoverage/-/jscoverage-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(expect.js)
BuildRequires:  npm(mocha)
BuildRequires:  npm(optimist)
BuildRequires:  npm(xfs)
BuildRequires:  uglify-js1
%endif

%description
%{summary}.


%prep
%setup -q -n package
%nodejs_fixdep uglify-js '1.3.x'
%nodejs_fixdep optimist '~0.4'
# Some files are executable that don't need to be.
find -type f -iname '*.js' -exec chmod 644 '{}' \;


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/jscoverage
cp -pr package.json index.js lib/ \
    %{buildroot}%{nodejs_sitelib}/jscoverage
mkdir -p %{buildroot}%{nodejs_sitelib}/jscoverage/bin
install -p -D -m0755 bin/jscoverage \
    %{buildroot}%{nodejs_sitelib}/jscoverage/bin/jscoverage
mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/jscoverage/bin/jscoverage %{buildroot}%{_bindir}

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha test/test.js
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/jscoverage
%{_bindir}/jscoverage


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.8-2
- fix uglify-js1 symlink

* Tue Sep 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.8-1
- update to upstream release 0.3.8

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.7-5
- restrict to compatible arches

* Fri May 31 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.7-4
- fix executable bit on some files

* Fri May 31 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.7-3
- fix uglify-js dependency and symlink

* Fri May 31 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.7-2
- fix versioned dependency on npm(optimist)

* Sun May 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.7-1
- update to upstream release 0.3.7
- upstream have now included a copy of the MIT license

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.5-3
- amend summary

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.5-2
- make use of %%nodejs_fixdep
- depend on uglify-js1 instead of uglify-js

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.5-1
- initial package
