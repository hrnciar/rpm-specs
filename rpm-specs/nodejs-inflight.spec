%{?scl:%scl_package nodejs-inflight}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:		%{?scl_prefix}nodejs-inflight
Version:	1.0.4
Release:	16%{?dist}
Summary:	Node.js inflight
License:	ISC
Url:		https://github.com/isaacs/inflight
Source:		http://registry.npmjs.org/inflight/-/inflight-%{version}.tgz
BuildRequires:	nodejs-packaging
BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	npm(wrappy)
BuildRequires:	npm(once)

%if 0%{?enable_tests}
BuildRequires:	npm(tap)
%endif

%description
Add callbacks to requests in flight to avoid async duplication 

%prep
%setup -q -n package

%{nodejs_fixdep} once
%{nodejs_fixdep} wrappy

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/inflight
cp -pr package.json inflight.js \
        %{buildroot}%{nodejs_sitelib}/inflight/

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tap test.js
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/inflight

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-5
- Removed redundant %%nodejs_fixdep macro

* Wed Apr 15 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-4
- Added BuildRequires, macros, %%license and %%check sections

* Tue Mar 03 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-3
- Fixed dependency
- removed BuildRoot, Group, %%defattr
- changed ExclusiveArch

* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-2
- Remove undefined macro

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-1
- Initial build

