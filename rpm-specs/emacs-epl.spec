%global pkg epl

Name:           emacs-%{pkg}
Version:        0.9
Release:        1%{?dist}
Summary:        Emacs Package Library

License:        GPLv3+
URL:            https://github.com/cask/%{pkg}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
%{summary}.


%prep
%autosetup -n %{pkg}-%{version}


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/


%files
%doc README.md
%license COPYING
%{_emacs_sitelispdir}/%{pkg}/


%changelog
* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9-1
- Initial RPM release
