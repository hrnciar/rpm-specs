%global pkg flycheck

Name:           emacs-%{pkg}
Version:        31
Release:        1%{?dist}
Summary:        On the fly syntax checking for GNU Emacs

License:        GPLv3+
URL:            https://www.flycheck.org/
Source0:        https://github.com/%{pkg}/%{pkg}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
BuildRequires:  emacs-dash
BuildRequires:  emacs-pkg-info
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-dash
Requires:       emacs-pkg-info
BuildArch:      noarch

%description
Flycheck is a modern on-the-fly syntax checking extension for GNU Emacs,
intended as replacement for the older Flymake extension which is part of GNU
Emacs.


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
%doc CHANGES.old CHANGES.rst MAINTAINERS README.md
%license COPYING
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 31-1
- Initial RPM release
