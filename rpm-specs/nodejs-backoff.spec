%{?nodejs_find_provides_and_requires}

%global packagename backoff
%global enable_tests 1

Name:		nodejs-backoff
Version:	2.5.0
Release:	6%{?dist}
Summary:	Fibonacci and exponential backoffs

License:	MIT
URL:		https://github.com/MathieuTurcotte/node-backoff
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	examples-%{version}.tar.bz2
Source2:	docs-%{version}.tar.bz2
Source10:	dl-tests.sh


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(precond)
%if 0%{?enable_tests}
BuildRequires:	npm(nodeunit)
BuildRequires:	npm(sinon)
%endif

%description
Fibonacci and exponential backoffs.


%prep
%autosetup -n package
# setup the tests
%autosetup -T -D -a 1 -n package
%autosetup -T -D -a 2 -n package

# fix script interpreter
sed -i '1s/env //' examples/*.js

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/nodeunit tests/
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md docs/ examples/
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 24 2017 Jared Smith <jsmith@fedoraproject.org> - 2.5.0-1
- Initial packaging