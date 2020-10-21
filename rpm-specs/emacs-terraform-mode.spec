%global pkg terraform-mode

Name:           emacs-%{pkg}
Version:        0.06
Release:        3%{?dist}
Summary:        Major mode of Terraform configuration file

License:        GPLv3+
URL:            https://github.com/syohex/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
BuildRequires:  emacs-hcl-mode
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-hcl-mode
BuildArch:      noarch

%description
Major mode of terraform configuration file. terraform-mode provides syntax
highlighting, indentation function and formatting.

Format the current buffer with terraform-format-buffer. To always format
terraform buffers when saving, use:

    (add-hook 'terraform-mode-hook 'terraform-format-on-save-mode)


%prep
%autosetup


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el


%files
%doc Changes README.md
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.06-1
- Initial RPM release
