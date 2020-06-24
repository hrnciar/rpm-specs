%{?scl:%scl_package nodejs-util-extend}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:		%{?scl_prefix}nodejs-util-extend
Version:	1.0.1
Release:	12%{?dist}
Summary:	Node's internal object extension function
License:	MIT
Url:		https://github.com/isaacs/util-extend
Source:		http://registry.npmjs.org/util-extend/-/util-extend-%{version}.tgz
Source1:	https://raw.githubusercontent.com/kasicka/util-extend/72ad112332507572d2c4dbe55f30b584a0d70878/LICENSE
		#https://github.com/isaacs/util-extend/pull/7
BuildRequires:	nodejs-packaging
BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

%description
The object extending function used with Node.js.

%prep
%setup -q -n package

cp -p %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/util-extend
cp -pr package.json extend.js \
	%{buildroot}%{nodejs_sitelib}/util-extend/

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
node test.js
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/util-extend

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Mar 14 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-4
- Removed Group, BuildRoot and %%defattr
- changed ExclusiveArch
- added %%check, %%nodejs_symlink_deps macro and %%license
- fixed nodejs-packaging dependency

* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-3
-  Remove undefined macro

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-2
- Add dist macro

* Tue Jan 06 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-1
- Initial build
