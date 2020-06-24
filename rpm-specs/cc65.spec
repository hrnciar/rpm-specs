# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Logic for creating an unversioned symlink to %%{_pkgdocdir}
# in case %%{_pkgdocdir} is actually a versioned directory.
# %%global doesn't work here as we need lazy expansion.
%define doc_symlink %{lua:if rpm.expand("%{_pkgdocdir}") ~= rpm.expand("%{_docdir}/%{name}") then print (1) end}

# Setup macros for compile flags if not defined already.
%{!?build_cflags:%global build_cflags %{optflags}}
%{!?build_ldflags:%global build_ldflags %{?__global_ldflags}}

# Construct the distribution string for BUILD_ID.
# Please alter them, if you are building packages
# for third-party repositories from this spec file.
%if 0%{?fedora}
%global dist_string Fedora
%else
%if 0%{?rhel}
%global dist_string Fedora EPEL
%else
%global dist_string UNKNOWN
%endif
%endif

# Some general used defines to reduce boilerplate.
%global git_url https://github.com/%{name}/%{name}

%global make_opts BUILD_ID="%{dist_string} %{version}-%{release}" \\\
LDFLAGS="%{build_ldflags}" USER_CFLAGS="%{build_cflags}"

%global dir_opts PREFIX="%{_prefix}" bindir="%{_bindir}" \\\
datadir="%{_datadir}/%{name}" htmldir="%{_pkgdocdir}/html" \\\
infodir="%{_infodir}"

# Run check target by default.
%bcond_without check


Name:           cc65
Version:        2.18
Release:        12%{?dist}
Summary:        A free C compiler for 6502 based systems

# For license clarification see:
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=714058#30
License:        zlib
URL:            https://cc65.github.io
Source0:        %{git_url}/archive/V%{version}/%{name}-%{version}.tar.gz

# Backported from upstream.
Patch0001:      0001-sim65-common-define-for-paravirt-hooks-base-location.patch
Patch0002:      0002-Reduced-shadow-for-h2-to-improve-readability.patch
Patch0003:      0003-Replace-GIT_SHA-with-a-more-versatile-BUILD_ID-defin.patch
Patch0004:      0004-test-ref-otccex-Fix-ramdomly-occurring-segfault.patch
Patch0005:      0005-util-zlib-deflater-Fix-several-compiler-warnings.patch
Patch0006:      0006-zlib-Use-correct-un-signedness-of-char-in-prototypes.patch
Patch0007:      0007-Made-the-ld65-configure-file-s-segment-offset-attrib.patch
Patch0008:      0008-Minor-URL-update.patch
Patch0009:      0009-src-Makefile-Simplify-BUILD_ID-logic.patch
Patch0010:      0010-Changed-empty-parameter-lists-into-void-lists-on-fun.patch
Patch0011:      0011-Add-page-0-variables-from-Telemon-2.4.patch
Patch0012:      0012-Add-XSCROH-XSCROB-value.patch
Patch0013:      0013-cc65-Add-support-for-binary-literals.patch
Patch0014:      0014-binlit-Add-a-few-random-leading-zeros.patch
Patch0015:      0015-Document-binary-literals.patch
Patch0016:      0016-Fix-bug-gotoxy-does-not-working-because-Y-does-not-u.patch
Patch0017:      0017-Add-textcolor-and-bgcolor.s.patch
Patch0018:      0018-Fix-gotoy-changecolor.patch
Patch0019:      0019-fix-typo.patch
Patch0020:      0020-fix-import.patch
Patch0021:      0021-Fix-typo-and-optimize.patch
Patch0022:      0022-Fix-label-optimize-code.patch
Patch0023:      0023-Fix-bug-with-bgcolor-and-textcolor.patch
Patch0024:      0024-jmp-instead-of-jsr.patch
Patch0025:      0025-Fix-bgcolor-and-textcolor-must-return-last-color-jmp.patch
Patch0026:      0026-Optimize-Clrscr.patch
Patch0027:      0027-Cleaning-import-variables.patch
Patch0028:      0028-Fix-comment-and-gotox-force-colour-change.patch
Patch0029:      0029-Fix-bug-FF.patch
Patch0030:      0030-Allowed-old-style-K-and-R-function-declarations-to-b.patch
Patch0031:      0031-Add-cclear-and-cclearxy.patch
Patch0032:      0032-Cleaning.patch
Patch0033:      0033-doc-clarify-need-for-.IMPORT-on-some-special-symbols.patch
Patch0034:      0034-Grammatical-modifications.patch
Patch0035:      0035-Use-the-word-macros-universally-not-macroes.patch
Patch0036:      0036-Added-a-charmap-header-that-converts-no-character-en.patch
Patch0037:      0037-Use-MACHID-to-check-for-realtime-clock.patch
Patch0038:      0038-Added-a-.ORG-keyword-to-ca65-structs-unions.patch
Patch0039:      0039-Created-a-target-and-a-library-for-the-Commander-X16.patch
Patch0040:      0040-Updated-the-cx16-start-up-to-the-emulator-s-release-.patch
Patch0041:      0041-Put-the-C64-code-into-cx16-_scrsize.s.patch
Patch0042:      0042-Fixed-a-typo-in-the-cx16-document.patch
Patch0043:      0043-Added-character-codes-to-change-between-the-two-CBM-.patch
Patch0044:      0044-Fixed-cgetc.patch
Patch0045:      0045-Made-the-none-CPU-allow-all-address-sizes.patch
Patch0046:      0046-Fix-Gamate-RVS.patch
Patch0047:      0047-Fix-colors-for-948.patch
Patch0048:      0048-Hello-world-example-for-the-Supervision.patch
Patch0049:      0049-Move-screen-init-into-crt0.s.patch
Patch0050:      0050-Improve-init-code-readability.patch
Patch0051:      0051-Improve-helloworld-example-for-Supervision.patch
Patch0052:      0052-Add-supervisionhello-in-samples-Makefile.patch
Patch0053:      0053-Use-decimal-for-lcd-size-initialization.patch
Patch0054:      0054-Comments.patch
Patch0055:      0055-Improve-comments.patch
Patch0056:      0056-Init-is-no-longer-in-crt0.s.patch
Patch0057:      0057-Significantly-faster-rand-implementation.patch
Patch0058:      0058-Update-comments-in-rand.s.patch
Patch0059:      0059-Added-new-program-descriptions-to-the-list.patch
Patch0060:      0060-Fixed-problems-with-the-Atari-Lynx-s-TGI-driver.patch
Patch0061:      0061-cx16-Update-ROM-banks-to-new-mapping.patch
Patch0062:      0062-Fixed-error-handling-for-missing-names-in-ld65-confi.patch
Patch0063:      0063-Fix-char-35-38-42-47-52.patch
Patch0064:      0064-Fix-4.patch
Patch0065:      0065-M-N-fixed.patch
Patch0066:      0066-Fix-left-arrow-char-77-13-64.patch
Patch0067:      0067-Fix-127-second-left-arrow.patch
Patch0068:      0068-small-m-and-n-fixed.patch
Patch0069:      0069-New-OSI-input-routine-based-on-disassembly-of-ROM-co.patch
Patch0070:      0070-Restructured-according-to-review.patch
Patch0071:      0071-Remove-obsolete-comment.patch
Patch0072:      0072-Remove-source-file-that-was-only-used-for-testing.patch
Patch0073:      0073-Address-review-comments.patch
Patch0074:      0074-Removed-redundant-LDA.patch
Patch0075:      0075-Added-the-GIF-switch-to-the-X16-emulator-s-control-p.patch
Patch0076:      0076-Tentative-solution-for-cgetc-in-Lynx.patch
Patch0077:      0077-Remove-useless-tax.patch
Patch0078:      0078-remove-bra.patch
Patch0079:      0079-Added-VERA-peek-and-poke-to-the-cx16-library.patch
Patch0080:      0080-libsrc-kplot.s-Use-cbm_kernal.inc-symbols-not-hardco.patch
Patch0081:      0081-vic20-cputc-Fix-incorrect-CRAM_PTR-at-startup-when-u.patch
Patch0082:      0082-Second-tentative-fix.patch
Patch0083:      0083-stz.patch
Patch0084:      0084-kbhit-checks-KBEDG-and-getc-resets-KBEDG.patch
Patch0085:      0085-Optimizations.patch
Patch0086:      0086-Reformat-comments-to-style-guide-rules.patch
Patch0087:      0087-Optimize-a-negation-in-signed-division.patch
Patch0088:      0088-Don-t-set-carry-when-already-set.patch
Patch0089:      0089-Swap-the-positive-negative-paths-to-save-a-branch.patch
Patch0090:      0090-Optimize-sign-extension.patch
Patch0091:      0091-Fixed-typos.patch
Patch0092:      0092-Made-assert-send-SIGABRT-when-an-assertion-fails.patch
Patch0093:      0093-Fixed-exit-code-974.patch
Patch0094:      0094-Changed-a-See-also-link-in-the-abort-and-assert-desc.patch
Patch0095:      0095-Updated-cx16-to-match-the-Commander-X16-ROMs-and-emu.patch
Patch0096:      0096-Added-a-standard-mouse-driver-to-the-cx16-library.patch
Patch0097:      0097-Fix-silent-crash-failure-on-warning-from-linker-comm.patch
Patch0098:      0098-make-linker-generated-export-warning-conistent-with-.patch
Patch0099:      0099-Replaced-plain-0-s-and-1-s-in-exit-statements-with-E.patch
Patch0100:      0100-Added-enum-for-cc65-exit-codes.-replaced-stdlib-exit.patch
Patch0101:      0101-Added-comment-to-debugger-exit-with-error.patch
Patch0102:      0102-Replaced-enum-in-cc65.h-by-defines.-added-comment-th.patch
Patch0103:      0103-Removed-CC65_-prefixes-from-exit-statements-in-abort.patch
Patch0104:      0104-Removed-additional-exit-constants-definitions-from-c.patch
Patch0105:      0105-added-additional-empty-line-after-header-guard-in-cc.patch
Patch0106:      0106-Removed-unnecessary-include-cc65.h-from-convert.c.patch
Patch0107:      0107-Fixed-C16-978.patch
Patch0108:      0108-Update-c16.sgml.patch
Patch0109:      0109-Update-c128.sgml.patch
Patch0110:      0110-Update-c64.sgml.patch
Patch0111:      0111-Update-cbm510.sgml.patch
Patch0112:      0112-Update-cx16.sgml.patch
Patch0113:      0113-Update-funcref.sgml.patch
Patch0114:      0114-Update-nes.sgml.patch
Patch0115:      0115-Update-pce.sgml.patch
Patch0116:      0116-Update-plus4.sgml.patch
Patch0117:      0117-Update-vic20.sgml.patch
Patch0118:      0118-Update-color.s.patch
Patch0119:      0119-Update-conio.s.patch
Patch0120:      0120-Update-cputc.s.patch
Patch0121:      0121-Update-fast.s.patch
Patch0122:      0122-Update-isfast.s.patch
Patch0123:      0123-Update-revers.s.patch
Patch0124:      0124-Update-slow.s.patch
Patch0125:      0125-Update-status.s.patch
Patch0126:      0126-Added-cx16.h-to-the-function-reference-document.patch
Patch0127:      0127-Expanded-Sim65-zero-page.patch
Patch0128:      0128-Changed-sim65-s-internal-error-codes-from-9-bit-valu.patch
Patch0129:      0129-Added-the-missing-BANK_RAM-array-to-the-Commander-X1.patch
Patch0130:      0130-Updated-the-cx16-library-to-the-Commander-X16-Kernal.patch
Patch0131:      0131-Made-the-program-chaining-exec-handle-the-X16-emulat.patch
Patch0132:      0132-Added-real-time-clock-functions-to-the-cx16-library.patch
Patch0133:      0133-Fixed-the-target-guards-around-the-usage-messages.patch
Patch0134:      0134-Made-ca65-give-error-messages-when-it-sees-duplicate.patch
Patch0135:      0135-Changes-in-INSTALL-routine-from-emd-c128-vdc.s.patch
Patch0136:      0136-Added-reservation-of-second-byte-for-pagecount.patch
Patch0137:      0137-Changed-the-order-in-which-lo-hi-bytes-of-vdc-addr-a.patch
Patch0138:      0138-Updated-the-cx16-library-to-the-ROM-s-prerelease-36.patch
Patch0139:      0139-Minor-cleanup.patch
Patch0140:      0140-Made-cc65-detect-a-possibly-missing-argument-at-the-.patch
Patch0141:      0141-added-regression-test-related-to-bug-1001.patch
Patch0142:      0142-store-y-first-then-a.-fix-by-willymanilly.patch
Patch0143:      0143-Fixes-Atari-OS-devhdl_t-init-field-needs-an-JMP-byte.patch
Patch0144:      0144-Corrected-check-in-OptTransfers2-for-register-usage..patch
Patch0145:      0145-Always-insert-a-LDA-after-the-removed-PLA-during-the.patch
Patch0146:      0146-Quick-fix-for-the-OptPushPop-bug-reported-in-Issue-3.patch
Patch0147:      0147-Just-disable-OptPushPop-if-N-Z-is-used-after-the-PLA.patch
Patch0148:      0148-ctype-size-optimization.patch
Patch0149:      0149-Changes-resulting-from-code-review.patch
Patch0150:      0150-Changes-resulting-from-2nd-code-review.patch
Patch0151:      0151-Fix-bug-in-tgi_line-HRS-X-parameters-are-16-bits.patch
Patch0152:      0152-Fix-16-bits-values.patch
Patch0153:      0153-Normalized-Atari-naming.patch
Patch0154:      0154-Fixed-a-typo-in-commit-2e5fbe89cd3f67b06b292936dfdf4.patch
Patch0155:      0155-Made-use-of-65C02-opcode-thx-to-polluks.patch
Patch0156:      0156-Fixed-an-error-message-printer.patch
Patch0157:      0157-SEGMENT-start-of-0-should-be-valid.patch
Patch0158:      0158-fix-whitespace.patch
Patch0159:      0159-Update-get_ostype.s.patch
Patch0160:      0160-Adjusted-comments-due-to-recent-change.patch
Patch0161:      0161-cc65-inline-asm-stp-mnemonic-support.patch
Patch0162:      0162-code-style.patch
Patch0163:      0163-Aligned-comment.patch
Patch0164:      0164-Added-missing-tag-and-itemize-Linuxdoc-tags-to-some-.patch
Patch0165:      0165-fix-the-clean-target-to-remove-any-disk-images.patch
Patch0166:      0166-Matched-comment-to-the-one-in-the-C-header-file.patch
Patch0167:      0167-Some-style-adjustments.patch
Patch0168:      0168-Adjusted-tolower-and-toupper-to-https-github.com-cc6.patch
Patch0169:      0169-Fixed-tolower-and-toupper-to-save-high-byte.patch
Patch0170:      0170-Shortened-names-and-adjusted-style.patch

BuildRequires:  gcc
BuildRequires:  make

Requires:       %{name}-common = %{version}-%{release}

%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Recommends:     %{name}-doc = %{version}-%{release}
Recommends:     %{name}-utils%{?_isa} = %{version}-%{release}
%endif

%description
cc65 is a complete cross development package for 65(C)02 systems,
including a powerful macro assembler, a C compiler, linker,
librarian and several other tools.

cc65 has C and runtime library support for many of the old 6502
machines, including

- the following Commodore machines:
  - VIC20
  - C16/C116 and Plus/4
  - C64
  - C128
  - CBM 510 (aka P500)
  - the 600/700 family
  - newer PET machines (not 2001).
- the Apple ]\[+ and successors.
- the Atari 8 bit machines.
- the Atari 2600 console.
- the Atari 5200 console.
- GEOS for the C64, C128 and Apple //e.
- the Bit Corporation Gamate console.
- the NEC PC-Engine (aka TurboGrafx-16) console.
- the Nintendo Entertainment System (NES) console.
- the Watara Supervision console.
- the VTech Creativision console.
- the Oric Atmos.
- the Oric Telestrat.
- the Lynx console.
- the Ohio Scientific Challenger 1P.


%package        devel
Summary:        Development files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-common = %{version}-%{release}

%description    devel
This package contains the development files needed to
compile and link applications for the 65(C)02 CPU with
the %{name} cross compiler toolchain.


%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

BuildRequires:  linuxdoc-tools
BuildRequires:  texinfo

%description    doc
This package contains the documentation files for %{name}.


%package        utils
Summary:        Additional utilities for %{name}
BuildRequires:  zlib-devel

%description    utils
This package contains the additional utilities for %{name}.

They are not needed for compiling applications with %{name},
but might be handy for some additional tasks.

Since these utility programs have some heavier dependencies,
and also can be used without the need of installing %{name},
they have been split into this package.


%prep
%autosetup -p 1


%build
# Parallel build sometimes fails.
# It finishes fine in a second run, tho.
%make_build %{make_opts} %{dir_opts} || \
%make_build %{make_opts} %{dir_opts}

# Build some additional utils.
%{__mkdir_p} util_bin
%{__cc} %{build_cflags} util/atari/ataricvt.c \
  -o util_bin/ataricvt65 %{build_ldflags}
%{__cc} %{build_cflags} util/cbm/cbmcvt.c \
  -o util_bin/cbmcvt65 %{build_ldflags}
%{__cc} %{build_cflags} util/gamate/gamate-fixcart.c \
  -o util_bin/gamate-fixcart65 %{build_ldflags}
%{__cc} %{build_cflags} util/zlib/deflater.c \
  -o util_bin/deflater65 %{build_ldflags} -lz

# Build the documentation.
%make_build doc


%install
%make_install %{make_opts} %{dir_opts}

# Install additional utils.
%{__install} -p -m 0755 util/ca65html %{buildroot}%{_bindir}
%{__install} -p -m 0755 util_bin/* %{buildroot}%{_bindir}

# Install more documentation.
%{__mv} %{buildroot}%{_datadir}/%{name}/samples %{buildroot}%{_pkgdocdir}
%{__install} -p -m 0644 README.md %{buildroot}%{_pkgdocdir}
%if !(0%{?fedora} >= 21 || 0%{?rhel} >= 7)
%{__install} -p -m 0644 LICENSE %{buildroot}%{_pkgdocdir}
%endif
%if 0%{doc_symlink}
%{__ln_s} %{_pkgdocdir} %{buildroot}%{_docdir}/%{name}
%endif


%if %{with check}
%check
# We need a clean build without PREFIX et all defined
# to successfully run the tests from inside the builddir.
# Unfortunately the testsuite cannot be run threaded.  -_-
%{__make} clean
%make_build %{make_opts} || \
%make_build %{make_opts}
%{__make} -C test QUIET=1
%endif


%files
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%license LICENSE
%else
%doc %{_pkgdocdir}/LICENSE
%endif
%if 0%{doc_symlink}
%doc %{_docdir}/%{name}
%endif
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%{_bindir}/ar65
%{_bindir}/ca65
%{_bindir}/cc65
%{_bindir}/chrcvt65
%{_bindir}/cl65
%{_bindir}/co65
%{_bindir}/da65
%{_bindir}/grc65
%{_bindir}/ld65
%{_bindir}/od65
%{_bindir}/sim65
%{_bindir}/sp65


%files devel
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}*
%else
%doc %{_pkgdocdir}/LICENSE
%endif
%if 0%{doc_symlink}
%doc %{_docdir}/%{name}
%endif
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%{_datadir}/%{name}


%files doc
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}*
%endif
%if 0%{doc_symlink}
%doc %{_docdir}/%{name}
%endif
%doc %{_pkgdocdir}
%{_infodir}/*.info*


%files utils
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}*
%else
%doc %{_pkgdocdir}/LICENSE
%endif
%if 0%{doc_symlink}
%doc %{_docdir}/%{name}
%endif
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%{_bindir}/ataricvt65
%{_bindir}/ca65html
%{_bindir}/cbmcvt65
%{_bindir}/deflater65
%{_bindir}/gamate-fixcart65


%changelog
* Mon Apr 06 2020 Björn Esser <besser82@fedoraproject.org> - 2.18-12
- Add several bugfix patches from upstream

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-10
- Add several bugfix patches from upstream

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-8
- Add a set of upstream patches to fix several minor bugs

* Mon Jul 15 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-7
- Add two upstream patches for minor fixes

* Fri Jul 05 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-6
- Clarify the purpose of the devel package in its %%description
  a bit more verbose

* Fri Jul 05 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-5
- Add an upstream patch to fix ld65 behaviour

* Sun Jun 23 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-4
- Add some stuff for backwards compatibility
- Add an unversioned symlink to %%{_pkgdocdir} if needed

* Wed Jun 19 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-3
- Replace Patch1000 with actual upstream commits

* Sat Jun 15 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-2
- Update Patch1000
- Add an option to disable %%check target

* Tue Jun 11 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-1
- Initial import (#1718684)

* Tue Jun 11 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-0.6
- Add a link for clarifying the actual license
- Remove the %%{name} prefix from binaries in the utils package
  and suffix them with 65 for a more uniform experience
- Add a few comments
- Optimize some global definitions to be more vasatile

* Tue Jun 11 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-0.5
- Fix use of a macro
- Remove hiphen separator from binaries in utils package
- Fix an entry in %%changelog

* Mon Jun 10 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-0.4
- Update Patch1000

* Mon Jun 10 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-0.3
- Adapt BUILD_ID to be architecture independent
- Drop Patches 1001 and 2000 as they are not needed anymore

* Sun Jun 09 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-0.2
- Add downstream patch to undefine a macro mangling version string

* Sat Jun 08 2019 Björn Esser <besser82@fedoraproject.org> - 2.18-0.1
- Initial rpm release (#1718684)
