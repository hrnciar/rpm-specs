%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-range-parser
Version:    1.2.0
Release:    6%{?dist}
Summary:    Range header field string parser for Node.js
License:    MIT
URL:        https://github.com/visionmedia/node-range-parser
Source0:    http://registry.npmjs.org/range-parser/-/range-parser-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:    https://raw.githubusercontent.com/jshttp/range-parser/v%{version}/test/range-parser.js

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
mkdir -p test/
cp -p %{SOURCE1} test/range-parser.js


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/range-parser
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/range-parser

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
%doc *.md
%license LICENSE
%{nodejs_sitelib}/range-parser


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Jared Smith <jsmith@fedoraproject.org> - 1.2.0-1
- Update to upstream 1.2.0 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 08 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.0-1
- update to usptream release 1.0.0

* Sun Jul 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.4-5
- restrict to compatible arches

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-4
- rebuild for missing npm(nodejs-range-parser) provides on EL6

* Thu Feb 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.4-3
- add copy of Readme.md from upstream that contains the license text

* Tue Feb 12 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.4-2
- document how to retrieve tests

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.4-1
- initial package
