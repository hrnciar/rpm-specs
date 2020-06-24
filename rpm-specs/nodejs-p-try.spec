%{?nodejs_find_provides_and_requires}

%global packagename p-try
# tests missing due to missing npm(ava)
%global enable_tests 0

Name: nodejs-p-try
Version: 2.0.0
Release: 1%{?dist}
Summary: Starts a promise chain
License: MIT
URL:     https://github.com/sindresorhus/p-try
Source0: https://github.com/sindresorhus/p-try/archive/v%{version}/%{packagename}-%{version}.tar.gz

BuildRequires: nodejs-packaging
ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:  noarch

%description
Starts a promise chain

%prep
%autosetup -n %{packagename}-%{version}

%build
# Nothing to do here

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/ava
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc readme.md
%license license
%{nodejs_sitelib}/%{packagename}

%changelog
* Sat Feb 15 2020 Sérgio Basto <sergio@serjux.com> - 2.0.0-1
- Initial RPM release, based on nodejs-p-try-2.0.0-1.mga8.src.rpm .
