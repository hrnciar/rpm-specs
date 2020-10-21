Name:          diffoscope
Version:       154
Release:       1%{?dist}
Summary:       In-depth comparison of files, archives, and directories
License:       GPLv3+
URL:           https://diffoscope.org/
#Source0:       https://files.pythonhosted.org/packages/source/d/diffoscope/diffoscope-%%{version}.tar.gz
Source0:       https://salsa.debian.org/reproducible-builds/diffoscope/-/archive/%{version}/diffoscope-%{version}.tar.gz

%global tools \
    acl \
    abootimg \
    black \
    e2fsprogs \
    cpio \
    llvm, llvm-devel \
    binutils \
    diffutils \
    gzip \
    unzip \
    bzip2 \
    xz \
    tar \
    zip \
    sng >= 1.1.0-2 \
    openssl \
    openssh \
    openssh-clients \
    sqlite \
    genisoimage \
    squashfs-tools \
    java-devel \
    /usr/bin/img2txt \
    /usr/bin/rpm2cpio \
    /usr/bin/msgunfmt \
    /usr/bin/ps2ascii \
    /usr/bin/qemu-img \
    /usr/bin/xxd \
    /usr/bin/ghc \
    /usr/bin/cd-iccdump \
    /usr/bin/oggDump \
    /usr/bin/Rscript \
    /usr/bin/fdtdump \
    /usr/bin/gifbuild \
    /usr/bin/dumppdf \
    /usr/bin/h5dump \
    gnupg \
    pgpdump \
    findutils \
    file \
    ImageMagick \
    poppler-utils \
    python3-debian \
    python3-h5py \
    python3-PyPDF2 \
    python3-magic \
    python3-pdfminer \
    python3-tlsh \
    python3-libarchive-c \
    gnumeric \
    odt2txt \
    wabt

# missing:
# apktool
# js-beautify
# /usr/bin/dumpxsb from xmlbeans-scripts, xmlbeans

%ifnarch ppc64 ppc64le
%global tools2 \
    coreboot-utils \
    mono-devel
%endif
%ifarch x86_64 i686 armv7hl
%global tools3 \
    fpc
%endif


%global toolz %(echo "%tools %?tools2 %?tools3" | grep . | tr '\\n' ', ')

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-docutils
# for tests
BuildRequires: python3-pytest
BuildRequires: %toolz
BuildRequires: help2man

# libguestfs is not installable in koji right now, ffs. Let's only require is at end user systems.
Requires:      python3-libguestfs
Recommends:    %toolz

%description
diffoscope will try to get to the bottom of what makes files or directories
different. It will recursively unpack archives of many kinds and transform
various binary formats into more human readable form to compare them. It can
compare two tarballs, ISO images, or PDF just as easily. The differences can
be shown in a text or HTML report.

diffoscope is developed as part of the "reproducible builds" Debian project and
was formerly known as "debbindiff".

%prep
%autosetup -p1
sed -i '1{\@/usr/bin/env@d}' diffoscope/main.py

sed -i s/python-magic/file-magic/ setup.py

%build
%py3_build
make -C doc

%install
%py3_install
echo %{buildroot}%{python3_sitelib}
install -Dm0644 -t %{buildroot}%{_mandir}/man1/ doc/diffoscope.1
install -Dm0644 -t %{buildroot}/usr/share/zsh/site-functions/ debian/zsh-completion/_diffoscope

%check
DESELECT=(
  # https://bugzilla.redhat.com/show_bug.cgi?id=1778875
  # https://salsa.debian.org/reproducible-builds/diffoscope/issues/9
  # https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=877724
  --deselect=tests/comparators/test_ppu.py::test_diff

  --deselect=tests/comparators/test_ppu.py::test_identification
  --deselect=tests/comparators/test_ppu.py::test_compare_non_existing

  # Debian has ocaml 4.08, we have 4.10/4.11. Might be the cause.
  --deselect=tests/comparators/test_ocaml.py::test_diff

  # Seems to be some incompatibility with python3.9
  --deselect=tests/comparators/test_wasm.py
)

LC_CTYPE=C.utf8 \
TZ=UTC \
PYTHONPATH=build/lib/ \
%{__python3} -m pytest tests/ -vv ${DESELECT[@]}

%files
%doc README.rst debian/changelog
%license COPYING
%{python3_sitelib}/diffoscope*
%{_bindir}/diffoscope
/usr/share/zsh/site-functions/_diffoscope
%doc %{_mandir}/man1/diffoscope.1*

%changelog
* Fri Aug  7 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 154-1
- Update to latest version
- Drop dependency on enjarify (#1841628). Hopefully only temporarily.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 137-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 137-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 137-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 137-2
- Rebuilt for Python 3.9

* Thu Mar  5 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 137-1
- Update to latest version, fix build (#1799281)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 134-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 134-1
- Update to latest version (bugfix changes only according to debian
  changelog)

* Sun Dec  1 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 133-1
- Update to latest version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 111-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 111-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 111-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 105-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 105-1
- Update to latest version

* Sat Sep 15 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 100-1
- Update to latest version
- Fix reference to file-magic (#1583331)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul  2 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 98-1
- Update to latest upstream version (declared python3.7 compat)

* Mon Jun 25 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 96-1
- Update to latest version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 95-2
- Rebuilt for Python 3.7

* Sun May 20 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 95-1
- Update to latest version
  (see https://salsa.debian.org/reproducible-builds/diffoscope/blob/516d5930f16867282d537c884e78213f9c4b8796/debian/changelog).

* Fri Mar  2 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 91-1
- Update to latest version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 90-1
- Update to latest version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 77-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 77-2
- Pull in enjarify

* Mon Feb 13 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 77-1
- Update to latest version (fixes #1421770, CVE-2017-0359)
- Also pull in python-debian

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 69-1
- Update to latest version (upstream dropped trydiffoscope)
- Add more dependendencies, and pull them in as Recommends

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 62-2
- Rebuild for Python 3.6

* Tue Nov 15 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 62-1
- Update to latest version

* Mon Aug 15 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 59-1
- Update to latest version
- Require python-libarchive-c (#1367034)

* Mon Aug 15 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 58-1
- Update to latest version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 54-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 10 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 54-1
- Update to latest version

* Thu Mar 10 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 51-3
- Change License to GPLv3+

* Thu Mar 10 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 51-2
- Require python3-tlsh

* Wed Mar  9 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 51-1
- Update to v 51
- Add man page

* Tue Mar  8 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 48-1
- Update to v 48, simplify packaging

* Sat Dec 05 2015 Dhiru Kholia <dhiru@openwall.com> - 42-1
- Initial version
