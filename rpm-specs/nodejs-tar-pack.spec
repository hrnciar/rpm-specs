%{?nodejs_find_provides_and_requires}

%global packagename tar-pack
%global enable_tests 1

Name:		nodejs-tar-pack
Version:	3.4.0
Release:	6%{?dist}
Summary:	Package and un-package modules of some sort (in tar/gz bundles)

License:	BSD
URL:		https://github.com/ForbesLindesay/tar-pack
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(debug)
BuildRequires:	npm(fstream)
BuildRequires:	npm(fstream-ignore)
BuildRequires:	npm(once)
BuildRequires:	npm(readable-stream)
BuildRequires:	npm(rimraf)
BuildRequires:	npm(tar)
BuildRequires:	npm(uid-number)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(mkdirp)
BuildRequires:	npm(rfile)
%endif

%description
Package and un-package modules of some sort (in tar/gz bundles).


%prep
%autosetup -n package

%nodejs_fixdep readable-stream

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Jared Smith <jsmith@fedoraproject.org> - 3.4.0-1
- Initial packaging
