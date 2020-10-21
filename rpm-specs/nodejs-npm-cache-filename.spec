%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:		nodejs-npm-cache-filename
Version:	1.0.2
Release:	11%{?dist}
Summary:	Return NPM cache folder
License:	ISC
Url:		https://github.com/npm/npm-cache-filename
Source:		http://registry.npmjs.org/npm-cache-filename/-/npm-cache-filename-%{version}.tgz
BuildRequires:	%{?scl_prefix}nodejs
BuildRequires:	nodejs-packaging
BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

%if 0%{?enable_tests}
BuildRequires:	npm(tap)
%endif

%description
Given a cache folder and url, return the appropriate cache folder. 

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/npm-cache-filename
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/npm-cache-filename/

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%tap test.js
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/npm-cache-filename

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Update to 1.0.2 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-5
- Removed scl prefixes

* Fri Mar 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-4
- Removed Group, BuildRoot and %%defattr
- changed ExclusiveArch
- added %%check, %%license and %%nodejs_symlink_deps macros and nodejs-packaging dependency

* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-3
- Remove undefined macro

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-2
- Add dist makro

* Tue Jan 06 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-1
- rebuilt

