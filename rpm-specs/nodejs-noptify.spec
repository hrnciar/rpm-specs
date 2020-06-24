%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-noptify
Version:    0.0.3
Release:    14%{?dist}
Summary:    A wrapper for the nopt module with a commander-like API
License:    MIT
URL:        https://github.com/mklabs/noptify
Source0:    http://registry.npmjs.org/noptify/-/noptify-%{version}.tgz
Source1:    https://raw.githubusercontent.com/mklabs/noptify/cfa11f776ddcd844a04982c0763df546621ce26a/LICENSE-MIT

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(nopt)
%endif

%description
%{summary}.


%prep
%setup -q -n package
cp -p %{SOURCE1} .

%nodejs_fixdep nopt


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/noptify
cp -pr package.json actions/ index.js util/ \
    %{buildroot}%{nodejs_sitelib}/noptify

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha --reporter spec
%endif


%files
%doc LICENSE-MIT readme.md
%{nodejs_sitelib}/noptify


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 25 2015 Jared Smith <jsmith@fedoraproject.org> - 0.0.3-6
- Relax version requirements on npm(nopt)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 30 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.3-2
- add BR: npm(nopt)

* Sat Mar 29 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.3-1
- initial package
