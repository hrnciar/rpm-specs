Name:		ricochet
Version:	1.1.4
Release:	22%{?dist}
Summary:	Anonymous peer-to-peer instant messaging

License:	BSD
URL:		https://ricochet.im/
Source0:	https://ricochet.im/releases/%{version}/ricochet-%{version}-src.tar.bz2
#Source0:	https://github.com/ricochet-im/%{name}/archive/1.1.3.tar.gz#/%{name}-1.1.3.tar.gz

BuildRequires:	openssl-devel
BuildRequires:	protobuf-compiler
BuildRequires:	protobuf-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtbase-gui
BuildRequires:	qt5-qtdeclarative-devel
BuildRequires:	qt5-qtmultimedia-devel
BuildRequires:	qt5-qtquickcontrols
BuildRequires:	qt5-qttools-devel
BuildRequires:	desktop-file-utils
Requires:	tor hicolor-icon-theme
Requires:	qt5-qtquickcontrols

%description
Ricochet is an experiment with a different kind of instant messaging that
doesn't trust anyone with your identity, your contact list, or your
communications.
* You can chat without exposing your identity (or IP address) to anyone
* Nobody can discover who your contacts are or when you talk (meta-data-free!)
* There are no servers to compromise or operators to intimidate for your
     information
* It's cross-platform and easy for non-technical users

Warnings: Tor does no protocol cleaning.  That means there is a danger
that application protocols and associated programs can be induced to
reveal information about the initiator. Tor depends on Privoxy and
similar protocol cleaners to solve this problem. The present network
is very small -- this further reduces the strength of the anonymity
provided. Tor is not presently suitable for high-stakes anonymity.


%prep
%setup -q

sed -i s/Qt/Qt\;/g src/ricochet.desktop

%build
%qmake_qt5 DEFINES+=RICOCHET_NO_PORTABLE CONFIG+=release
sed -i "s|\$(INSTALL_ROOT)/usr|\$(INSTALL_ROOT)%{_prefix}|g" Makefile.Release
make -f Makefile.Release %{?_smp_mflags}


%install
make -f Makefile.Release install INSTALL_ROOT=%{buildroot}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications src/ricochet.desktop

%files
%{_bindir}/ricochet
%{_datadir}/applications/ricochet.desktop
%{_datadir}/icons/hicolor/48x48/apps/ricochet.png
%exclude %{_datadir}/icons/hicolor/scalable/apps/ricochet.svg
%doc AUTHORS.md README.md
%license LICENSE


%changelog
* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 1.1.4-22
- Rebuilt for protobuf 3.13

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.1.4-20
- Rebuilt for protobuf 3.12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1.1.4-18
- Rebuild for protobuf 3.11

* Fri Aug 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.1.4=17
- Drop giant svg icon.

* Thu Aug 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.1.4-16
- Desktop file handling tweak.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.4-13
- Rebuild for protobuf 3.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.4-10
- Remove obsolete scriptlets

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.1.4-9
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.4-8
- Rebuild for protobuf 3.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.1.4-5
- Rebuild for protobuf 3.3.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Orion Poplawski <orion@cora.nwra.com> - 1.1.4-3
- Rebuild for protobuf 3.2.0

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 1.1.4-2
- Rebuild for protobuf 3.1.0

* Mon Nov 07 2016 Jon Ciesla <limburgher@gmail.com> 1.1.4-1
- 1.1.4

* Wed Oct 12 2016 Jon Ciesla <limburgher@gmail.com> 1.1.3-1
- 1.1.3

* Thu Jun 09 2016 Jon Ciesla <limburgher@gmail.com> 1.1.2-2
- Fixed icon scriptlets and desktop file for review.

* Fri Apr 22 2016 Jon Ciesla <limburgher@gmail.com> 1.1.2-1
- 1.1.2
- Added manual qt5-qtquickcontrols Requires.

* Mon Sep 21 2015 Jon Ciesla <limburgher@gmail.com> 1.1.1-2
- Fixed description, macros for review.

* Sun Sep 20 2015 Jon Ciesla <limburgher@gmail.com> 1.1.1-1
- Initial RPM Package based on upstream spec.
