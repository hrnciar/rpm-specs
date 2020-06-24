%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-iso8601
Version:    1.1.1
Release:    16%{?dist}
Summary:    Node.js module to parse and print ISO8601 dates
License:    MIT
URL:        https://github.com/calmh/node-iso8601
Source0:    http://registry.npmjs.org/iso8601/-/iso8601-%{version}.tgz

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
%{summary}


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/iso8601
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/iso8601

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha -R spec
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/iso8601


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.1-5
- restrict to compatible arches

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-4
- rebuild for missing npm(iso8601) provides on EL6

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.1-3
- %%nodejs_fixdep not actually needed

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.1-2
- make use of %%nodejs_fixdep

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.1-1
- initial package
