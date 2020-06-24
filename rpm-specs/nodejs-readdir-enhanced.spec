%{?nodejs_find_provides_and_requires}

%global packagename readdir-enhanced

# Tests fail in NodeJS 10.x
%global enable_tests 0

Name:		nodejs-readdir-enhanced
Version:	2.2.1
Release:	5%{?dist}
Summary:	A fs.readdir with sync, async, and streaming APIs

License:	MIT
URL:		https://github.com/bigstickcarpet/readdir-enhanced.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source{1-9} are generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source10:	dl-tests.sh


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(call-me-maybe)
BuildRequires:	npm(glob-to-regexp)

%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(chai)
BuildRequires:	npm(del)
BuildRequires:	npm(mkdirp)
BuildRequires:	npm(through2)
%endif

%description
A fs.readdir with sync, async, and streaming APIs + filtering, recursion,
absolute paths, etc.


%prep
%autosetup -n package
# setup the tests
%autosetup -T -D -a 1 -n package


%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
NODE_ENV=test %{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2.2.1-1
- Initial packaging