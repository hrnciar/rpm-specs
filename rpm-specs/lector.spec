Name:       lector
Summary:    Ebook reader and collection manager
URL:        https://github.com/BasioMeusPuga/Lector
Version:    0.5.1
Release:    1%{?dist}
BuildArch:  noarch

# Lector uses GPLv3, the bundled Rarfile library uses the MIT license.
License: GPLv3 and MIT

Source0: https://github.com/BasioMeusPuga/Lector/archive/%{version}/%{name}-%{version}.tar.gz
Source1: https://raw.githubusercontent.com/terrycloth/Lector/packaging/lector/resources/raw/io.github.BasioMeusPuga.Lector.metainfo.xml

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: python3dist(beautifulsoup4) >= 4.6
BuildRequires: python3-devel >= 3.6
BuildRequires: python3-poppler-qt5 >= 0.24.2
BuildRequires: python3-PyQt5 >= 5.10.1
BuildRequires: python3dist(setuptools)
BuildRequires: pkgconfig(Qt)

Requires: hicolor-icon-theme
Requires: python3 >= 3.6
Requires: python3dist(beautifulsoup4) >= 4.6
Requires: python3dist(lxml) >= 4.3
Requires: python3-poppler-qt5 >= 0.24.2
Requires: python3dist(pymupdf) >= 1.14.5
Requires: python3-PyQt5 >= 5.10.1
Requires: python3dist(xmltodict) >= 0.11

Recommends: python3dist(python-djvulibre) >= 0.8.4
Recommends: python3dist(markdown) >= 3.0.1
Recommends: python3dist(textile) >= 3.0.4

%description
Lector is an ebook reader and collection manager. It offers a
full-screen distraction-free view, document highlighting and
annotations, a built-in dictionary, bookmarks, and multiple profiles for
changing the way the books are presented. Lector can also edit metadata,
so you can correct information about the books, and add keywords to make
them easier to find.

It supports the following file formats:

* PDF
* EPUB
* DjVu
* FictionBook (.fb2)
* Mobipocket (.mobi)
* Amazon Kindle (.azw, .azw3, .azw4)
* Comic book archives (.cbr, .cbz)
* Markdown




%prep
%autosetup -n Lector-%{version}
# These files contain a Python shebang, but seem to get installed by upstream's setup.py without an executability bit set, so there's a mismatch in whether it's supposed to be executable...
chmod -x ./lector/KindleUnpack/compatibility_utils.py
chmod -x ./lector/KindleUnpack/mobi_split.py
chmod -x ./lector/KindleUnpack/unipath.py
chmod -x ./lector/__main__.py
chmod -x ./lector/rarfile/dumprar.py
# Non-executable Python files don't need a shebang line.
find ./  -type f  -iname "*.py"  '!' -executable  -exec sed --regexp-extended 's|^#! */usr/bin/env python[[:digit:]._-]*$||g'  --in-place '{}' ';'
# For executable Python files, don't use env python.
find ./  -type f  -iname "*.py"  -executable  -exec sed --regexp-extended 's|^#! */usr/bin/env python[[:digit:]._-]*$|#!%{__python3}|g'  --in-place '{}' ';'



%build
%py3_build
mv  ./lector/rarfile/LICENSE  ./LICENSE-rarfile



%install
%py3_install
# NOTE: Upstream hasn't merged the .metainfo.xml file nor renamed the .desktop to match, yet.
mkdir -p %{buildroot}/%{_metainfodir}/
cp --archive  %{SOURCE1}  %{buildroot}/%{_metainfodir}/
mv  %{buildroot}/%{_datadir}/applications/lector.desktop  %{buildroot}/%{_datadir}/applications/io.github.BasioMeusPuga.Lector.desktop



%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/io.github.BasioMeusPuga.Lector.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/io.github.BasioMeusPuga.Lector.metainfo.xml



%files
%doc      AUTHORS  README.md
%license  LICENSE  LICENSE-rarfile
%{_bindir}/%{name}
%{_datadir}/applications/io.github.BasioMeusPuga.Lector.desktop
%{_datadir}/icons/hicolor/scalable/apps/Lector.png
%{_metainfodir}/io.github.BasioMeusPuga.Lector.metainfo.xml
%{python3_sitelib}/lector*



%changelog
* Wed Dec 18 2019 Andrew Toskin <andrew@tosk.in> - 0.5.1-1
- First (mostly) working build.
