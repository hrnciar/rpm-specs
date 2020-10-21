%global pkg auto-complete

Name:           emacs-%{pkg}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Emacs auto-complete package

License:        GPLv3+
URL:            https://github.com/%{pkg}/%{pkg}/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
BuildRequires:  emacs-popup
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-popup
BuildArch:      noarch

%description
Auto-Complete is an intelligent auto-completion extension for Emacs. It extends
the standard Emacs completion interface and provides an environment that allows
users to concentrate more on their own work.


%prep
%autosetup -n %{pkg}-%{version}


%build
for i in *.el; do
    %{_emacs_bytecompile} $i
done


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 *.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el


%files
%doc README.md
%license COPYING.GPLv3
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.5.1-1
- Initial RPM release
