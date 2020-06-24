%{?nodejs_find_provides_and_requires}

%global packagename needle
# Tests disabled until npm(jschardet) is packaged
%global enable_tests 0

Name:		nodejs-needle
Version:	1.5.2
Release:	7%{?dist}
Summary:	The leanest and most handsome HTTP client in the Nodelands

License:	MIT
# License file requested upstream at https://github.com/tomas/needle/issues/152
URL:		https://github.com/tomas/needle.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Patch0:		nodejs-needle_fix-tests.patch

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(debug)
%if 0%{?enable_tests}
BuildRequires:	npm(jschardet)
BuildRequires:	npm(q)
BuildRequires:	npm(should)
BuildRequires:	npm(sinon)
BuildRequires:	npm(xml2js)
BuildRequires:	mocha
%endif

Requires:	nodejs

%description
The leanest and most handsome HTTP client in the Nodelands.


%prep
%setup -q -n package
%patch0 -p1

# fix script interpreter
sed -i '1s;env node;node;' bin/needle

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json  lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}/bin
install -p -D -m0755 bin/needle %{buildroot}%{nodejs_sitelib}/%{packagename}/bin/needle

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{packagename}/bin/needle \
    %{buildroot}%{_bindir}/needle


%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
mkdir -p test/keys
openssl genrsa -out test/keys/ssl.key 2048
openssl req -new -key test/keys/ssl.key -x509 -subj /CN=test@example.com -days \
999 -out test/keys/ssl.cert
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md examples/
%license license.txt
%{nodejs_sitelib}/%{packagename}
%{_bindir}/needle



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 24 2017 Jared Smith <jsmith@fedoraproject.org> - 1.5.2-1
- Update to upstream 1.5.2 release

* Sat Jan 07 2017 Jared Smith <jsmith@fedoraproject.org> - 1.4.3-1
- Update to upstream 1.4.3 release

* Mon Nov 30 2015 Jared Smith <jsmith@fedoraproject.org> - 0.11.0-1
- Initial packaging
