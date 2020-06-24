%{?nodejs_find_provides_and_requires}

%global packagename read-cmd-shim
%global enable_tests 1

Name:		nodejs-read-cmd-shim
Version:	1.0.1
Release:	10%{?dist}
Summary:	Figure out what a cmd-shim is pointing at

License:	ISC
URL:		https://github.com/npm/read-cmd-shim.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	LICENSE-ISC.txt
# license file requested upstream at https://github.com/npm/read-cmd-shim/issues/1

Patch0:		read-cmd-shim_fix-tests.patch
# patch to fix the tests, submitted upstream at https://github.com/npm/read-cmd-shim/pull/2

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	npm(cmd-shim)
BuildRequires:  npm(graceful-fs)
BuildRequires:	npm(rimraf)
BuildRequires:	npm(tap)
%endif

%description
Figure out what a cmd-shim is pointing at. This acts as the equivalent of
fs.readlink.


%prep
%setup -q -n package
cp -p %{SOURCE1} .
%patch0 -p1


%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%{_bindir}/tap test/*.js
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE-ISC.txt
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 31 2015 Tom Hughes <tom@compton.nu> - 1.0.1-2
- Require npm(graceful-fs) for tests

* Thu Dec 17 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.1-1
- Initial packaging
