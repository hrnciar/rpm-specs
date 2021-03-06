%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-wordwrap
Version:        1.0.0
Release:        10%{?dist}
Summary:        Word wrapping library for node

License:        MIT
URL:            https://github.com/substack/node-wordwrap
Source0:        https://registry.npmjs.org/wordwrap/-/wordwrap-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tape)
%endif

%description
Wrap those words. Show them at what columns to start and stop.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/wordwrap
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/wordwrap

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
ln -sf .. node_modules/wordwrap
%{_bindir}/tape test/*.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc README.markdown example
%license LICENSE
%{nodejs_sitelib}/wordwrap

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Update to upstream 1.0.0 release
- Switch from expresso to tape for test suite, as expresso isn't maintained

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.0.2-8
- cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.2-4
- restrict to compatible arches
- enable tests

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-2
- fix License tag

* Fri Jan 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-1
- initial package generated by npm2rpm
