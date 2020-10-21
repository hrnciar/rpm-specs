%global pkg pkg-info

Name:           emacs-%{pkg}
Version:        0.6
Release:        1%{?dist}
Summary:        Provide information about Emacs packages

License:        GPLv3+
URL:            https://github.com/lunaryorn/%{pkg}.el/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
BuildRequires:  emacs-epl
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-epl
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

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el


%files
%doc README.md
%license COPYING
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6-1
- Initial RPM release
