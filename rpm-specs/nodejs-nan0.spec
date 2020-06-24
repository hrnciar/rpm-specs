%{?nodejs_find_provides_and_requires}

Name:              nodejs-nan0
Version:           0.8.0
Release:           12%{?dist}
Summary:           Native Abstractions for Node.js
License:           MIT
URL:               http://github.com/rvagg/nan
Source0:           http://registry.npmjs.org/nan/-/nan-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

# nan is a header only library statically included by dependents
Provides:      %{name}-devel = %{version}-%{release}
Provides:      %{name}-static = %{version}-%{release}

BuildRequires:     nodejs-packaging

%description
A header file filled with macro and utility goodness
for making add on development for Node.js easier across
versions 0.8, 0.10 and 0.11, and eventually 0.12.

Thanks to the crazy changes in V8 (and some in Node core),
keeping native add-on compiling happily across versions,
particularly 0.10 to 0.11/0.12, is a minor nightmare.
The goal of this project is to store all logic necessary
to develop native Node.js add-on without having to inspect
NODE_MODULE_VERSION and get yourself into a macro-tangle.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/nan@0
cp -pr package.json include_dirs.js nan.h \
    %{buildroot}%{nodejs_sitelib}/nan@0


%files
%doc LICENSE README.md
%{nodejs_sitelib}/nan@0


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.0-2
- comply with the header only library policy

* Sat May 10 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.0-1
- initial package
