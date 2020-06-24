%{?nodejs_find_provides_and_requires}

%global packagename kind-of
%global enable_tests 1

Name:		nodejs-kind-of
Version:	3.2.2
Release:	7%{?dist}
Summary:	Get the native type of a value

License:	MIT
URL:		https://github.com/jonschlinkert/kind-of.git
Source0:	https://github.com/jonschlinkert/kind-of/archive/%{version}/kind-of-%{version}.tar.gz
BuildArch:	noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(is-buffer)
BuildRequires:	npm(should)
%endif


%description
Get the native type of a value.


%prep
%autosetup -n kind-of-%{version}

%nodejs_fixdep is-buffer

%build
# nothing to do!


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo "Tests disabled..."
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Jared K. Smith <jsmith@fedoraproject.org> - 3.2.2-3
- Relax dependency on npm(is-buffer)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 15 2017 Jared Smith <jsmith@fedoraproject.org> - 3.2.2-1
- Update to upstream 3.2.2 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Tom Hughes <tom@compton.nu> - 3.1.0-3
- Update to 3.1.0 upstream release

* Fri Feb 12 2016 Jared Smith <jsmith@fedoraproject.org> - 3.0.2-3
- Remove some BuildRequires that are not needed

* Thu Feb  4 2016 Jared Smith <jsmith@fedoraproject.org> - 3.0.2-2
- Initial packaging
