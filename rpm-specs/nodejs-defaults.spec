%{?scl:%scl_package nodejs-defaults}
%{!?scl:%global pkg_name %{name}}

%global npm_name defaults
%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:		nodejs-defaults
Version:	1.0.3
Release:	9%{?dist}
Summary:	Merge single level defaults over a config object
Url:		https://github.com/tmpvar/defaults
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT
BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:  npm(clone)
BuildRequires:	nodejs-devel
BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(tap)
%endif

%description
Merge single level defaults over a config object

%prep
%setup -q -n package

%{nodejs_fixdep} tap

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
node test.js
%endif

%files
%{nodejs_sitelib}/defaults

%doc README.md
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 27 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.3-2
- Bump

* Thu Oct 27 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.3-1
- Update

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-2
- Added %%nodejs_fixdep macro to fix failing dependency

* Fri May 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-1
- Rebuilt with new upstream release containing license text
- minor changes

* Tue Mar 17 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-3
- Added %%check, %%license, nodejs-clone dependency
- changed ExclusiveArch
- removed Group, BuildRoot and %%defattr
- fixed dependency on nodejs-packaging

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- Initial build

