Name:		rcm
Version:	1.3.3
Release:	6%{?dist}
Summary:	Management suite for dotfiles

License:	BSD
URL:		https://github.com/thoughtbot/rcm
Source0:	https://thoughtbot.github.io/rcm/dist/%{name}-%{version}.tar.gz

BuildArch:	noarch

%description
A suite of tools for managing dot-files (.zshrc, .vimrc, etc.).  This suite is
useful for committing your .*rc files to a central repository to share, but it
also scales to a more complex situation such as multiple source directories
shared between computers with some host-specific or task-specific files.

%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_mandir}/man{1,5,7}/*
%{_datadir}/rcm


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 8 2018 Link Dupont <linkdupont@fedoraproject.org> - 1.3.3-3
- Update summary

* Tue Nov 6 2018 Link Dupont <linkdupont@fedoraproject.org> - 1.3.3-2
- Tidy up files section

* Thu Nov 1 2018 Link Dupont <linkdupont@fedoraproject.org> - 1.3.3-1
- New upstream release

* Fri Jul 14 2017 Link Dupont <linkdupont@fedoraproject.org> - 1.3.1-1
- New upstream release

* Fri Jun 17 2016 Link Dupont - 1.3.0-1
- Initial package
