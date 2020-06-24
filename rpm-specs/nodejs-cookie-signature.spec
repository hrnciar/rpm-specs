%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-cookie-signature
Version:    1.0.6
Release:    6%{?dist}
Summary:    Node.js module to sign and unsign cookies
License:    MIT
URL:        https://github.com/tj/node-cookie-signature
Source0:    http://registry.npmjs.org/cookie-signature/-/cookie-signature-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:    tests-%{version}.tar.bz2
Source10:   dl-tests.sh

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(should)
%endif

%description
%{summary}.


%prep
%setup -q -n package
%setup -q -T -D -a 1 -n package

sed -e '0,/^## License/d' Readme.md > LICENSE

%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/cookie-signature
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/cookie-signature

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec --require should
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc History.md Readme.md
%license LICENSE
%{nodejs_sitelib}/cookie-signature


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.6-1
- Update to upstream 1.0.6 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 08 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.3-1
- update to upstream release 1.0.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.1-2
- rebuild for missing npm(cookie-signature) provides on EL6

* Wed Apr 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.1-1
- update to upstream release 1.0.1

* Mon Apr 15 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.0-1
- update to upstream release 1.0.0

* Tue Feb 12 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.1-2
- document how to retrieve "Source1: index-test.js"

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.1-1
- initial package
