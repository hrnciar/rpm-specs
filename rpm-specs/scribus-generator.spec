#Versioning for scribus
#%%global versioning 1.5.3.svn/
Name:		scribus-generator
Version:	2.9
Release:	2%{?dist}
Summary:	Open source high-quality PDF template and mail-merge alternative

License:	MIT
URL:		https://github.com/berteh/ScribusGenerator

Source0:	https://github.com/berteh/ScribusGenerator/archive/%{version}.tar.gz#/ScribusGenerator-%{version}.tar.gz
Source1:	%{name}.metainfo.xml

BuildRequires:	libappstream-glib
BuildRequires:	pkgconfig(python3)
Requires:	python3-tkinter
Requires:	scribus

BuildArch:	noarch

%description
Mail-Merge-like extension to Scribus, to generate Scribus and 
PDF documents automatically from external data.

%prep
%autosetup -n ScribusGenerator-%{version}

#Replace shebangs line #!/usr/bin/env python
sed -i 's/\r//' ScribusGeneratorBackend.py

%build
#Nothing to builds

%install
install -Dpm 0644 *.{py,conf} -t %{buildroot}%{_datadir}/scribus/scripts/
cp -r {example,pic} %{buildroot}%{_datadir}/scribus/scripts/


# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%license LICENSE
%doc README.md
%{_datadir}/scribus/scripts/*
#AppStream metadata
%{_metainfodir}/%{name}.metainfo.xml


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 22 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 2.9-1
- Update to 2.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.1-4
- Stop obsoleting and providing tkinter (#1768831)

* Sat Oct 26 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 2.8.1-3
- Obsolete tkinter and in favor of python3-tkinter for upgrade dependencies
- Use available pkgconf for python3 devel

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1
- Use metainfo path macro

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 2.8-1
- Update to 2.8

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6-2
- Rebuilt for Python 3.7

* Mon May 14 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 2.6-1
- Update to 2.6
- Switched to python3 build requirement rather than python2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 2.5-4
- Add missing loggin.conf file

* Thu Jan 18 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 2.5-4
- Remove conditional script version
- Add missing directory for frontend

* Sun Dec 17 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.5-3
- Fix source url

* Fri Dec 01 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.5-2
- Fix source url
- Add python2-devel for build requirement
- Fix overall spec

* Sun May  7 2017 Luya Tshimbalanga <luya@fedoraproject.org> 2.5-1
- Initial build
