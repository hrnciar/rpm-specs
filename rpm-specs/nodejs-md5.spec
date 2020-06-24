%{?nodejs_find_provides_and_requires}

%global packagename md5
%global enable_tests 1

Name:		nodejs-md5
Version:	2.2.1
Release:	6%{?dist}
Summary:	Javascript function for hashing messages with MD5

License:	BSD
URL:		https://github.com/pvorb/node-md5
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz


BuildArch:	noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch

BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:  npm(charenc)
BuildRequires:  npm(crypt)
BuildRequires:  npm(is-buffer)
%endif

%description
Javascript function for hashing messages with MD5.


%prep
%autosetup -n package

%nodejs_fixdep is-buffer

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json md5.js \
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
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2.2.1-2
- Relax dependency on npm(is-buffer)

* Wed Feb 21 2018 Jared Smith <jsmith@fedoraproject.org> - 2.2.1-1
- Initial packaging
