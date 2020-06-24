%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-has-color
Version:    0.1.7
Release:    11%{?dist}
Summary:    Detects whether a terminal supports color
License:    MIT
URL:        https://github.com/sindresorhus/has-color
Source0:    http://registry.npmjs.org/has-color/-/has-color-%{version}.tgz
Source1:    https://raw.githubusercontent.com/sindresorhus/has-color/ab671b1f74846d9fb9caea8dc302603a865be3cc/test.js
# https://github.com/sindresorhus/has-color/pull/4
Source2:    LICENSE

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
%endif

%description
%{summary}.


%prep
%setup -q -n package
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/has-color
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/has-color

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha
%endif


%files
%doc LICENSE readme.md
%{nodejs_sitelib}/has-color


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.7-1
- update to upstream release 0.1.7

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.4-1
- initial package
