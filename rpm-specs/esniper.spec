Name:           esniper
Version:        2.35.0
Release:        6%{?dist}
Summary:        A lightweight console application for sniping eBay auctions 

License:        BSD
URL:            http://esniper.sourceforge.net
%global dashver %(echo -n %{version} | tr '.' '-')
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{dashver}.tgz

BuildRequires:  gcc
BuildRequires:  curl-devel

%description
Esniper is a lightweight console application for sniping eBay auctions.


%prep
%setup -q -n %{name}-%{dashver}

# Encode manpage to utf-8
iconv -f iso8859-1 -t utf-8 esniper.1 > esniper.1.conv \
    && touch -r esniper.1 esniper.1.conv \
    && mv esniper.1.conv esniper.1


%build
%configure
make %{?_smp_mflags}


%install
make install INSTALL="install -p" DESTDIR=%{buildroot}

# Install frontend script
install -p -m 755 frontends/snipe %{buildroot}/%{_bindir}


%files
%doc frontends/README COPYING ChangeLog AUTHORS sample_config.txt sample_auction.txt
%{_bindir}/%{name}
%{_bindir}/snipe
%{_mandir}/man1/%{name}.1.*


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.35.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.35.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.35.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.35.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.35.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Volker Fröhlich <volker27@gmx.at> - 2.35.0-1
- New upstream release

* Thu Feb 08 2018 Volker Fröhlich <volker27@gmx.at> - 2.33.0-5
- Remove Group keyword

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.33.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.33.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.33.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Volker Fröhlich <volker27@gmx.at> - 2.33.0-1
- New upstream release
- Define a macro to translate the dots in the version to dashes

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Volker Fröhlich <volker27@gmx.at> - 2.32.0-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Volker Fröhlich <volker27@gmx.at> - 2.31.0-1
- New upstream release

* Fri May 23 2014 Volker Fröhlich <volker27@gmx.at> - 2.30.0-1
- New upstream release

* Wed Apr 02 2014 Volker Fröhlich <volker27@gmx.at> - 2.29.0-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Volker Fröhlich <volker27@gmx.at> - 2.28.0-1
- New upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Volker Fröhlich <volker27@gmx.at> - 2.27.0-1
- New upstream release
- Remove curl fix from previous release (included upstream)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 09 2011 Volker Fröhlich <volker27@gmx.at> - 2.26.0-2
- Don't include curl's types.h

* Tue Aug 09 2011 Volker Fröhlich <volker27@gmx.at> - 2.26.0-1
- Update for 2.26.0
- Drop defattr

* Sun Jun 05 2011 Volker Fröhlich <volker27@gmx.at> - 2.25.0-1
- Updated for 2.25.0

* Fri Feb 25 2011 Volker Fröhlich <volker27@gmx.at> - 2.24.0-6
- Added the INSTALL definition, that should have been there in the last release

* Fri Feb 25 2011 Volker Fröhlich <volker27@gmx.at> - 2.24.0-5
- Preserve timestamp on man page
- Defined INSTALL for make

* Thu Feb 24 2011 Volker Fröhlich <volker27@gmx.at> - 2.24.0-4
- Added sample aution file
- More specific files section

* Fri Dec 03 2010 Volker Fröhlich <volker27@gmx.at> - 2.24.0-3
- Added sample configuration to docs
- Install frontend script
- Shortened file list syntax

* Thu Dec 02 2010 Volker Fröhlich <volker27@gmx.at> - 2.24.0-2
- Dropped clean section and rm command from install section,
  as it's no longer necessary
- Replaced .gz with * for man-file
- Adapted source link

* Sun Nov 28 2010 Volker Fröhlich <volker27@gmx.at> - 2.24.0-1
- Inital packaging
