%global realname providers
%global upstream tsloughter

Name:     erlang-%{realname}
Version:  1.8.1
Release:  6%{?dist}
Summary:  An Erlang providers library
License:  LGPLv3
URL:      https://github.com/%{upstream}/%{realname}
# Use `generate-tarball.sh $VERSION` to fetch the sources from hex.pm
Source0:  %{realname}-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  erlang-rebar

%description
%{summary}.

%prep
%autosetup -n %{realname}-%{version}

%build
%{erlang_compile}

%install
%{erlang_install}

%check
%{erlang_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 08 2019 Timothée Floure <fnux@fedoraproject.org> - 1.8.1-1
- New upstream release
- Fix typos in previous changelog entry
- Fetch source0 from hex.pm instead of github

* Fri Mar 08 2019 Timothée Floure <fnux@fedoraproject.org> - 1.7.0-3
- Make package arch-independent
- Remove runtime dependency on erlang-rebar

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Timothée Floure <fnux@fedoraproject.org> - 1.7.0-1
- Let there be package
