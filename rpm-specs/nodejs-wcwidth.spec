%{?scl:%scl_package nodejs-wcwidth}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:		%{?scl_prefix}nodejs-wcwidth
Version:	1.0.0
Release:	15%{?dist}
Summary:	Port of C's wcwidth() and wcswidth()
License:	MIT
Url:		https://www.npmjs.com/package/wcwidth
Source:		http://registry.npmjs.org/wcwidth/-/wcwidth-%{version}.tgz
BuildRequires:	nodejs-packaging
BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

%if 0%{enable_tests}
BuildRequires:	npm(tape)
%endif

BuildRequires:	npm(defaults)

%description
Determine columns needed for a fixed-size wide-character string.

%prep
%setup -q -n package
%{nodejs_fixdep} defaults

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/wcwidth
cp -pr package.json index.js combining.js \
	%{buildroot}%{nodejs_sitelib}/wcwidth/

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tape test/*.js
%endif

%files
%doc docs/index.md Readme.md
%license LICENSE
%{nodejs_sitelib}/wcwidth

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 23 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-6
- Moved nodejs-defaults dependency outside conditional

* Fri Mar 20 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-5
- Added npm(defaults) to test dependencies
- fixed URL

* Tue Mar 10 2015 Zuzana Svetlikova - 1.0.0-4
- Removed Group, BuildRoot and %%defattr
- changed ExclusiveArch
- added %%nodejs_fixdep, %%license and %%check

* Wed Feb 25 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-3
- Fixed dependency on nodejs-packaging

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- Initial build
