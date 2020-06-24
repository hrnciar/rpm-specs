Name:           plowshare
Version:        2.0.1
Release:        10%{?dist}
Summary:        Download and upload files from file-sharing websites
Summary(pt_BR): Baixe e carregue arquivos em sites de compartilhamento
Summary(ru):    терминальный аплоадер/доунлоадер для наиболее популярных файлообменников
License:        GPLv3+
URL:            http://plowshare.googlecode.com
Source0:        https://plowshare.googlecode.com/archive/v%{version}.tar.gz


BuildRequires: git

Requires:  curl
Requires:  caca-utils
Requires:  recode
Requires:  js

BuildArch: noarch

%description
plowshare is a command-line downloader/uploader for some of the most popular
file-sharing websites. It works on UNIX-like systems and presently supports
Megaupload, Rapidshare, 2Shared, 4Shared, ZShare, Badongo, Depositfiles,
Mediafire, Netload.in, Storage.to, Uploaded.to, Uploading.com, Sendspace,
Usershare, X7.to and others.

%description -l pt_BR
plowshare é um cliente em linha de comando para baixar/carregar arquivos nos
mais populares sites de compartilhamento. Funciona em sistemas Unix-like e
atualmente suporta o Megaupload, RapidShare, 2Shared, 4Shared, Zshare, Badongo,
Depositfiles, Mediafire, Netload.in, Storage.to, Uploaded.to, Uploading.com,
Sendspace, Usershare, X7.to e outros.

%description -l ru
plowshare это терминальный аплоадер/доунлоадер для наиболее популярных файло-
обменников. Он работает на большинстве UNIX-подобных систем. На данный момент
поддерживаются следующие сервисы: Megaupload, Rapidshare, 2Shared, 4Shared,
ZShare, Badongo, DepositFiles и Mediafire. Смотрите README для подробностей.

%prep
%setup -q -n %{name}-v%{version}

%build
# Nothing to build, it's simple bash scripts

%install
rm -rf %{buildroot}
export PLOWSHARE_FORCE_VERSION=%{version}
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install

# We remove at destination, so we still have install
# for the doc section
rm -rf %{buildroot}%{_docdir}/%{name}4

%files
%doc AUTHORS README COPYING
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/bash-completion/
%{_mandir}/man1/*
%{_mandir}/man5/%{name}.conf.5.*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 08 2015 Elder Marco <eldermarco@fedoraproject.org> - 2.0.1-1
- Update to new version
- Modules are not available in this package anymore. This package deal
- with plowshare "core" only, as suggested by upstream.

* Sat Nov 08 2014 Elder Marco <eldermarco@fedoraproject.org> - 1.0.6-1
- Update to new upstream version, 1.0.6
- Force version with environment variable PLOWSHARE_FORCE_VERSION

* Sun Jul 27 2014 Elder Marco <eldermarco@fedoraproject.org> - 1.0.4-1
- Update to new upstream version

* Thu Apr 10 2014 Elder Marco <eldermarco@fedoraproject.org> - 1.0.1-1
- New upstream version
- Fix changelog in spec file
- New way to install the package

* Sun Jan 19 2014 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.46.20140112git
- New upstream snapshot

* Fri Nov 08 2013 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.45.20131102git
- New upstream snapshot

* Wed Sep 04 2013 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.44.20130901git
- New upstream snapshot

* Sat Aug 10 2013 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.43.20130727git
- New upstream snapshot

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-0.42.20130520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.41.20130520git
- New upstream snapshot

* Sun Jan 27 2013 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.40.20130126git
- New upstream snapshot

* Thu Jan 03 2013 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.39.20121230git
- New upstream snapshot

* Tue Nov 27 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.38.20121126git
- New upstream snapshot

* Sun Nov 04 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.37.20121104git
- New upstream snapshot

* Tue Sep 18 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.36.20120916git
- New upstream snapshot

* Sun Sep 02 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.35.20120901git
- New upstream snapshot

* Tue Aug 07 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.34.20120807git
- New upstream snapshot

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-0.33.20120707git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 07 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.32.20120707git
- New upstream snapshot
- Dropped dependencies ImageMagick and tesseract:
    http://code.google.com/p/plowshare/issues/detail?id=638

* Sat Jun 09 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.31.20120609git
- New upstream snapshot

* Sat May 12 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.30.20120511git
- New upstream snapshot

* Mon Apr 09 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.29.20120409git
- New upstream snapshot

* Sun Mar 11 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.28.20120311git
- New upstream snapshot

* Sat Feb 25 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.27.20120225git
- New upstream snapshot

* Wed Feb 01 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.26.20120130git
- New upstream snapshot

* Sun Jan 15 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.25.20120115git
- New upstream snapshot

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-0.24.20111230git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 30 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.23.20111230git
- New upstream snapshot

* Tue Dec 06 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.22.20111206git
- New upstream snapshot

* Wed Nov 23 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.21.20111117git
- New upstream snapshot

* Tue Nov 15 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.20.20111114git
- New upstream snapshot

* Thu Nov 10 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.19.20111030git
- Update to new upstream snapshot

* Thu Oct 27 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.18.20111023git
- Update to new upstream snapshot

* Fri Oct 07 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.17.20110926git
- Update to new upstream snapshot
- Fixed CDIR path in programmable completion file

* Sun Sep 25 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.16.20110918git
- Update to new upstream snapshot
- File plowshare.completion renamed to plowshare

* Thu Sep 15 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.15.20110914git
- New upstream snapshot

* Tue Sep 06 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.14.20110904git
- New upstream snapshot

* Mon Aug 29 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.13.20110828git
- New upstream snapshot

* Wed Aug 17 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.12.20110816git
- Update to new upstream snapshot
- Add Brazilian Portuguese Translation (summary and description)
- New file from upstream: plowshare.completion
- Upstream is now using git instead of svn

* Tue Aug  9 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.11.svn1657
- Update to new upstream snapshot
- New manpage from upstream: plowshare.conf.5
- Another cosmetic change in spec file

* Sun Jul 31 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.10.svn1645
- New upstream snapshot
- File AUTHORS is now UTF-8

* Mon Jul 25 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.9.svn1630
- Update to new upstream snapshot
- New documentation file from upstream: AUTHORS
- Using iconv to convert character encoding for file AUTHORS from iso8859-1
  to utf-8.

* Sun Jul 17 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.8.svn1591
- Update to new upstream revision
- Removed dependency perl(Image::Magick). It's not necessary.

* Tue Jul 12 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.7.svn1575
- Update to new upstream revision
- Cosmetics changes in spec file

* Sun Apr 24 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.4-0.6.svn1414
- Update to svn revision 1414 by request of Elder Marco by mail.

* Wed Mar 23 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.4-0.5.svn1394
- Update to new upstream revision (last befor import into Fedora).

* Mon Feb 28 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.4-0.4.svn1358
- Remove R gocr.

* Sun Feb 27 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.4-0.3.svn1358
- Delete bash from dependencies as it is common (thanks to Elder Marco).
- Fix summary.

* Sat Feb 26 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.4-0.2.svn1358
- Add BR perl(Image::Magick) and caca-utils (thanks to Elder Marco).

* Wed Feb 23 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.4-0.1.svn1358
- Update to last version.
- Adopt to upstream svn snapshots.
- Delete examples.
- lib.sh renamed to core.sh

* Tue Oct 5 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.3-2
- New version 0.9.3.
- Remove part %%{_prefix} from DESTDIR var and move it in new PREFIX one for
  script setup.sh
- Add files:
    o %%{_bindir}/plowlist and %%{_datadir}/%%{name}/list.sh
    o %%{_datadir}/%%{name}/tesseract
    o %%{_datadir}/%%{name}/strip_single_color.pl
    o %%{_datadir}/%%{name}/strip_threshold.pl
- Do not list all modules separately instead own full directory
  %%{_datadir}/%%{name}/modules/
- Add require gocr.
- Include mans: %%{_mandir}/man1/plow*.1*
- Include examples dir into %%doc and delete it from path where it installed
  automatically.

* Fri Nov 20 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.8.1-1
- Initial packaging.
- Optional requires aaview is not in Fedora repos. FR to support cacview
  filled:
  http://code.google.com/p/plowshare/issues/list?thanks=58&ts=1258746820
