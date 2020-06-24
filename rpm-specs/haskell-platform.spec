# https://fedoraproject.org/wiki/Packaging:Haskell

%global stack_ver 2.1.3.1
%global stack stack-%{stack_ver}

%global filelock filelock-0.1.1.4
%global hifileparser hi-file-parser-0.1.0.0
%global hpack hpack-0.31.2
%global httpdownload http-download-0.1.0.1
%global mintty mintty-0.1.2
%global mustache mustache-2.3.1
%global neatinterpolation neat-interpolation-0.3.2.6
%global openbrowser open-browser-0.2.1.0
%global pantry pantry-0.1.1.2
%global projecttemplate project-template-0.2.0.1
%global regexapplicativetext regex-applicative-text-0.1.0.1
%global retry retry-0.8.1.0

%global inferlicense infer-license-0.2.0
%global rioorphans rio-orphans-0.1.1.0
%global thutilities th-utilities-0.2.3.1

%global subpkgs %{filelock} %{hifileparser} %{inferlicense} %{hpack} %{retry} %{httpdownload} %{mintty} %{mustache} %{neatinterpolation} %{openbrowser} %{thutilities} %{rioorphans} %{pantry} %{projecttemplate} %{regexapplicativetext} %{stack}

Name:           haskell-platform
Version:        2020.1
Release:        2%{?dist}
Summary:        Standard Haskell distribution

License:        BSD
URL:            http://www.haskell.org/platform/
# for stack:
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{stack}/%{stack}.tar.gz
Source1:        https://hackage.haskell.org/package/%{filelock}/%{filelock}.tar.gz
Source2:        https://hackage.haskell.org/package/%{hifileparser}/%{hifileparser}.tar.gz
Source3:        https://hackage.haskell.org/package/%{hpack}/%{hpack}.tar.gz
Source4:        https://hackage.haskell.org/package/%{httpdownload}/%{httpdownload}.tar.gz
Source5:        https://hackage.haskell.org/package/%{mintty}/%{mintty}.tar.gz
Source6:        https://hackage.haskell.org/package/%{mustache}/%{mustache}.tar.gz
Source7:        https://hackage.haskell.org/package/%{neatinterpolation}/%{neatinterpolation}.tar.gz
Source8:        https://hackage.haskell.org/package/%{openbrowser}/%{openbrowser}.tar.gz
Source9:        https://hackage.haskell.org/package/%{pantry}/%{pantry}.tar.gz
Source10:       https://hackage.haskell.org/package/%{projecttemplate}/%{projecttemplate}.tar.gz
Source11:       https://hackage.haskell.org/package/%{regexapplicativetext}/%{regexapplicativetext}.tar.gz
Source12:       https://hackage.haskell.org/package/%{retry}/%{retry}.tar.gz
Source20:       https://hackage.haskell.org/package/%{inferlicense}/%{inferlicense}.tar.gz
Source21:       https://hackage.haskell.org/package/%{rioorphans}/%{rioorphans}.tar.gz
Source22:       https://hackage.haskell.org/package/%{thutilities}/%{thutilities}.tar.gz
# End cabal-rpm sources
Patch0:          stack-2.1-relax_version_warnings.patch

BuildRequires:  ghc
BuildRequires:  alex
BuildRequires:  cabal-install
BuildRequires:  happy
BuildRequires:  hscolour

# for stack:
# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-annotated-wl-pprint-prof
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-colour-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-conduit-extra-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cryptonite-prof
BuildRequires:  ghc-cryptonite-conduit-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-echo-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-extra-prof
BuildRequires:  ghc-file-embed-prof
#BuildRequires:  ghc-filelock-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-fsnotify-prof
BuildRequires:  ghc-generic-deriving-prof
BuildRequires:  ghc-githash-prof
BuildRequires:  ghc-hackage-security-prof
BuildRequires:  ghc-hashable-prof
#BuildRequires:  ghc-hi-file-parser-prof
#BuildRequires:  ghc-hpack-prof
BuildRequires:  ghc-hpc-prof
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-client-tls-prof
BuildRequires:  ghc-http-conduit-prof
#BuildRequires:  ghc-http-download-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-memory-prof
BuildRequires:  ghc-microlens-prof
#BuildRequires:  ghc-mintty-prof
BuildRequires:  ghc-mono-traversable-prof
BuildRequires:  ghc-mtl-prof
#BuildRequires:  ghc-mustache-prof
#BuildRequires:  ghc-neat-interpolation-prof
BuildRequires:  ghc-network-uri-prof
#BuildRequires:  ghc-open-browser-prof
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-optparse-simple-prof
#BuildRequires:  ghc-pantry-prof
BuildRequires:  ghc-path-prof
BuildRequires:  ghc-path-io-prof
BuildRequires:  ghc-persistent-prof
BuildRequires:  ghc-persistent-sqlite-prof
BuildRequires:  ghc-persistent-template-prof
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-process-prof
#BuildRequires:  ghc-project-template-prof
#BuildRequires:  ghc-regex-applicative-text-prof
BuildRequires:  ghc-resource-pool-prof
BuildRequires:  ghc-resourcet-prof
#BuildRequires:  ghc-retry-prof
BuildRequires:  ghc-rio-prof
BuildRequires:  ghc-rio-prettyprint-prof
BuildRequires:  ghc-semigroups-prof
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-tar-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-terminal-size-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-text-metrics-prof
BuildRequires:  ghc-th-reify-many-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-tls-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-typed-process-prof
BuildRequires:  ghc-unicode-transforms-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-unliftio-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-yaml-prof
BuildRequires:  ghc-zip-archive-prof
BuildRequires:  ghc-zlib-prof
# for missing dep 'hi-file-parser':
BuildRequires:  ghc-binary-prof
# for missing dep 'hpack':
BuildRequires:  ghc-Glob-prof
BuildRequires:  ghc-bifunctors-prof
#BuildRequires:  ghc-infer-license-prof
BuildRequires:  ghc-scientific-prof
# for missing dep 'mustache':
BuildRequires:  ghc-cmdargs-prof
BuildRequires:  ghc-either-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-th-lift-prof
# for missing dep 'neat-interpolation':
BuildRequires:  ghc-megaparsec-prof
# for missing dep 'pantry':
BuildRequires:  ghc-base-orphans-prof
BuildRequires:  ghc-contravariant-prof
BuildRequires:  ghc-digest-prof
BuildRequires:  ghc-network-prof
#BuildRequires:  ghc-rio-orphans-prof
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-syb-prof
BuildRequires:  ghc-tar-conduit-prof
BuildRequires:  ghc-th-lift-prof
BuildRequires:  ghc-th-lift-instances-prof
BuildRequires:  ghc-th-orphans-prof
#BuildRequires:  ghc-th-utilities-prof
# for missing dep 'regex-applicative-text':
BuildRequires:  ghc-regex-applicative-prof
# for missing dep 'retry':
BuildRequires:  ghc-random-prof
# End cabal-rpm deps

# pull in all of ghc for least surprise
# even though strictly libHSghc is not formally part of HP
Requires:       ghc
Requires:       alex
Requires:       cabal-install
Requires:       happy
Requires:       hscolour
Requires:       stack
# F26:
Obsoletes:      ghc-haskell-platform-devel < %{version}-%{release}

%description
Haskell Platform is a set stable and well used Haskell tools.
It provides a good starting environment for Haskell development.


%package -n stack
Version:        %{stack_ver}
Summary:        Haskell package tool
License:        BSD
Url:            http://haskellstack.org
Requires:       zlib-devel

%description -n stack
Stack is a cross-platform program for developing Haskell projects.


%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l CC0 %{filelock}
%ghc_lib_subpackage -l BSD  %{hifileparser}
%ghc_lib_subpackage -l MIT %{hpack}
%ghc_lib_subpackage -l BSD %{httpdownload}
%ghc_lib_subpackage -l BSD %{mintty}
%ghc_lib_subpackage -l BSD %{mustache}
%ghc_lib_subpackage -l MIT %{neatinterpolation}
%ghc_lib_subpackage -l BSD %{openbrowser}
%ghc_lib_subpackage -l BSD %{pantry}
%ghc_lib_subpackage -l BSD %{projecttemplate}
%ghc_lib_subpackage -l BSD %{regexapplicativetext}
%ghc_lib_subpackage -l BSD %{retry}
%ghc_lib_subpackage -l MIT %{inferlicense}
%ghc_lib_subpackage -l MIT %{rioorphans}
%ghc_lib_subpackage -l MIT %{thutilities}
%ghc_lib_subpackage -l BSD %{stack}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -c -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a20 -a21 -a22
# End cabal-rpm setup
%patch0 -b .orig
(
cd %{regexapplicativetext}
cabal-tweak-dep-ver base '<4.10' '<4.13'
)


%build
# Begin cabal-rpm build:
%ghc_libs_build %{subpkgs}
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_libs_install %{subpkgs}
%ghc_fix_rpath %{pkgver}
# End cabal-rpm install

# open-browser
rm %{buildroot}%{_bindir}/example
echo %{_bindir}/hpack >> %{hpack}/ghc-hpack.files
echo %{_bindir}/haskell-mustache >> %{mustache}/ghc-mustache.files


%files


%files -n stack
# Begin cabal-rpm files:
%license %{stack}/LICENSE
%doc %{stack}/CONTRIBUTING.md %{stack}/ChangeLog.md %{stack}/README.md
%{_bindir}/stack
# End cabal-rpm files


%changelog
* Sun Apr 12 2020 Jens Petersen <petersen@redhat.com> - 2020.1-2
- stack requires ghc-zlib-devel for ghc
- stack: silence warnings about ghc-8.8 and Cabal-3.0

* Wed Apr  8 2020 Jens Petersen <petersen@redhat.com> - 2020.1-1
- subpackage stack package tool

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May  9 2019 Jens Petersen <petersen@redhat.com> - 2019.1-2
- move obsoletes to ghc-obsoletes to not pull in this heavy package

* Wed May  8 2019 Jens Petersen <petersen@redhat.com> - 2019.1-1
- haskell-platform is now just a meta-package
- obsolete previous subpackaged Haskell Platform libraries
- package is now noarch

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.8.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 2018.8.2.2-14
- refresh to lts-11

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.8.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Jens Petersen <petersen@redhat.com> - 2017.8.2.2-12
- remove _isa from buildrequires (#1545187)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.8.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb  5 2018 Jens Petersen <petersen@redhat.com> - 2017.8.2.2-10
- update to upstream 8.2.2 release

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 2017.8.0.2-9
- rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.8.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.8.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Jens Petersen <petersen@redhat.com> - 2017.8.0.2-6
- enable prof libraries

* Fri Mar 10 2017 Jens Petersen <petersen@redhat.com> - 2017.8.0.2-5
- update to 8.0.2
- 'cgi' and 'multipart' dropped, add 'fixed'
- core haskell-platform now just provides tools
- drop ghc-haskell-platform-devel subpackage

* Fri Feb 10 2017 Jens Petersen <petersen@redhat.com> - 2016.7.10.3-4
- subpackage build like for other packages

* Wed Sep 28 2016 Jens Petersen <petersen@redhat.com> - 2016.7.10.3-3
- rebuild

* Fri Jul 29 2016 Jens Petersen <petersen@redhat.com> - 2016.7.10.3-2
- split-0.2.3.1
- use new ghc_libs_build and ghc_libs_install macros
- disable GL packages for armv7hl (#1372527)

* Thu Jun 23 2016 Jens Petersen <petersen@redhat.com> - 2016.7.10.3-1
- update to new haskell-platform version 7.10.3
- new half multipart ObjectName StateVar subpackages
- haskell98 dropped and cgi is back
- old-locale and old-time packages added
- bump version to 2016 for version bumps and to avoid epoch
- alex-3.1.7, async-2.1.0, attoparsec-0.13.0.2, cabal-install-1.22.9.0,
  HUnit-1.3.1.1, network-uri 2.6.1.0, parallel-3.2.1.0, parsec-3.1.11,
  QuickCheck-2.8.2, scientific-0.3.4.7, split-0.2.3, text-1.2.2.1, zlib-0.6.1.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2014.2.0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.2.0.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Jens Petersen <petersen@redhat.com> - 2014.2.0.0.3-4
- bump cabal-install to 1.18.1.0 and allow newer versions

* Fri Apr 10 2015 Jens Petersen <petersen@redhat.com> - 2014.2.0.0.2-3
- workaround build-tools version detection failures on aarch64 (#1210323)

* Fri Apr  3 2015 Jens Petersen <petersen@redhat.com> - 2014.2.0.0.2-2
- bump alex to 3.1.4
- bump cabal-install to 1.18.0.8
- bump happy to 1.19.5
- bump QuickCheck to 2.7.6

* Fri Feb  6 2015 Jens Petersen <petersen@redhat.com> - 2014.2.0.0.1-1
- use ghc-7.8.4
- bump attoparsec to 0.11.3.4
- bump text to 1.1.1.3

* Wed Aug 20 2014 Jens Petersen <petersen@redhat.com> - 2014.2.0.0-1
- update to haskell-platform-2014.2
- ghc-7.8.3+ ships xhtml
- cgi dropped
- requires hscolour

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-37
- rebuild for F21

* Mon Apr 21 2014 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-36
- fix build for versioned docdirs

* Mon Apr 21 2014 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-35
- alex and syb are separate packages again

* Mon Apr 14 2014 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-34
- cabal-install, happy, parallel, regex-compat are now separate packages

* Thu Mar 27 2014 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-33
- transformers lib is now separate package

* Wed Mar 26 2014 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-32
- QuickCheck and HTTP are separate packages again

* Mon Mar 17 2014 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-31
- HUnit is a separate package again
- network is a separate package again

* Thu Feb  6 2014 Jens Petersen <petersen@redhat.com>
- only show cabal-install upgrade notice for verbose

* Mon Feb  3 2014 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-30
- parsec is now a separate package again
- async is now a new separate package

* Wed Jan  8 2014 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-29
- regex-posix is now a separate package

* Fri Jan  3 2014 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-28
- html and regex-base are now separate packages

* Wed Dec  4 2013 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-27
- mtl and zlib are now separate packages again

* Thu Oct 31 2013 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-26
- fix alex patching for ppc and s390 archs

* Sat Oct 26 2013 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-25
- random and stm are separate packages again

* Fri Jul 26 2013 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-24
- fix packaging of license files when building without shared libraries
- tweaks for F20 unversioned docdir

* Sat May  4 2013 Jens Petersen <petersen@redhat.com> - 2013.2.0.0-23
- update to 2013.2.0.0
- new packages: GLURaw, OpenGLRaw
- new depends: attoparsec, case-insensitive, hashable, unordered-containers
- use ghc_fix_dynamic_rpath
- text lib is separate package again

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.4.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec  6 2012 Jens Petersen <petersen@redhat.com> - 2012.4.0.0-21
- vector was patched to build on all archs (#883479)

* Wed Dec  5 2012 Jens Petersen <petersen@redhat.com> - 2012.4.0.0-20
- keep split, vector, and primitive in their own existing src packages
- allow building on ghc archs without ghci: ie without vector library (#883479)

* Sat Oct 20 2012 Jens Petersen <petersen@redhat.com> - 2012.4.0.0-19
- update to 2012.4.0.0
- new subpackages: async, split, vector, and primitive (vector dep)
- drop explicit BR hscolour

* Mon Jul 23 2012 Jens Petersen <petersen@redhat.com> - 2012.2.0.0-18
- also apply the alex fix-bang-pattern patch for s390 and s390x

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.2.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 2012.2.0.0-16
- change prof BRs to devel

* Thu Jun  7 2012 Jens Petersen <petersen@redhat.com> - 2012.2.0.0-15
- update to 2012.2.0.0
- build the whole of haskell-platform now from this package
  and subpackage like ghc's libraries
- add alex fix-bang-pattern.diff patch from Debian to fix build on ppc archs
  - requires BR alex
- drop common_summary and common_description for subpackaging
- no longer need to unset debug_package
- make sure all the dynamically linked files get stripped
- needs ghc-rpm-macros 0.95.2 or later to build
- use chrpath to fix the program RPATHs when dynamically linked to HP libs

* Wed May  9 2012 Jens Petersen <petersen@redhat.com> - 2011.4.0.741-2
- update cabal-install to 0.14.0

* Sat Mar 24 2012 Jens Petersen <petersen@redhat.com> - 2011.4.0.741-1
- update to ghc-7.4.1 and latest libraries
- temporarily just a meta-package

* Wed Mar 21 2012 Jens Petersen <petersen@redhat.com> - 2011.4.0.0-7
- require ghc-compiler instead of ghc to avoid the ghc lib

* Fri Jan 20 2012 Jens Petersen <petersen@redhat.com> - 2011.4.0.0-6
- update to cabal2spec-0.25.2

* Thu Jan 19 2012 Jens Petersen <petersen@redhat.com> - 2011.4.0.0-5
- update the description

* Thu Jan 19 2012 Jens Petersen <petersen@redhat.com> - 2011.4.0.0-4
- update the source url

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jan  1 2012 Jens Petersen <petersen@redhat.com> - 2011.4.0.0-2
- define ghc_without_shared since ghc-haskell-platform-devel no longer
  requires ghc-haskell-platform

* Wed Dec 28 2011 Jens Petersen <petersen@redhat.com> - 2011.4.0.0-1
- update to 2011.4.0.0
- reenable ppc64
- drop ghc-haskell-platform subpackage
- require ghc-libraries instead of ghc-devel

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 2011.2.0.1-2
- ghc_arches replaces ghc_excluded_archs (cabal2spec-0.23.2)

* Mon Jun 20 2011 Jens Petersen <petersen@redhat.com> - 2011.2.0.1-1
- update to 2011.2.0.1: ghc-7.0.3 and text-0.11.0.6
- update source url
- use ghc_excluded_archs
- exclude ppc64: no QuickCheck
- bump ghc to 7.0.4
- use top_prefix for path to haskell-platform subdir in large tarball
- drop upstream_version

* Fri May 27 2011 Jens Petersen <petersen@redhat.com> - 2011.2.0.0-5
- drop the prof subpackage

* Wed May 25 2011 Jens Petersen <petersen@redhat.com> - 2011.2.0.0-4
- add ppc64 arch

* Mon Mar 28 2011 Jens Petersen <petersen@redhat.com> - 2011.2.0.0-3
- remove duplicate license file from ghc-haskell-platform

* Mon Mar 28 2011 Jens Petersen <petersen@redhat.com> - 2011.2.0.0-2
- fix the install scripts:
- ghc_reindex_haddock is now redundant
- use ghc_pkg_recache

* Fri Mar 11 2011 Jens Petersen <petersen@redhat.com> - 2011.2.0.0-1
- 2011.2.0.0 final

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 2011.1.0.0-0.6
- Enable build on sparcv9

* Tue Feb 15 2011 Jens Petersen <petersen@redhat.com> - 2011.1.0.0-0.5
- update to latest haskell-platform-2011.1 snapshot

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.1.0.0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 22 2011 Jens Petersen <petersen@redhat.com> - 2011.1.0.0-0.3
- make ghc-haskell-platform-devel require ghc-devel and ghc_devel_requires
- build with ghc_lib_build and without_haddock

* Tue Jan 18 2011 Jens Petersen <petersen@redhat.com> - 2011.1.0.0-0.2
- update to cabal2spec-0.22.4

* Sun Dec  5 2010 Jens Petersen <petersen@redhat.com> - 2011.1.0.0-0.1
- update to 2011.1.0.0 alpha snapshot

* Fri Nov 26 2010 Jens Petersen <petersen@redhat.com> - 2010.2.0.0.701-1
- bump some versions for ghc-7.0.1
- add hscolour
- no haddock documentation to build
- remove duplicate LICENSE file

* Fri Jul 23 2010 Jens Petersen <petersen@redhat.com> - 2010.2.0.0-1
- update to 2010.2.0.0 final release (no actual changes)

* Sun Jul 18 2010 Jens Petersen <petersen@redhat.com> - 2010.2.0.0-0.1
- drop debuginfo again: ghc_strip_dynlinked got fixed in ghc-rpm-macros-0.8.1

* Fri Jul 16 2010 Jens Petersen <petersen@redhat.com> - 2010.2.0.0-0.1
- update to 2010.2.0.0 RC
- obsolete ghc-haskell-platform-doc in line with ghc-rpm-macros-0.8.0
- add License to base library too

* Sun Jun 27 2010 Jens Petersen <petersen@redhat.com> - 2010.1.0.0.6123-1
- bump ghc to 6.12.3
- sync cabal2spec-0.22.1
- enable debugging for now to avoid empty strip error

* Thu Apr 29 2010 Jens Petersen <petersen@redhat.com> - 2010.1.0.0.6122-1
- break haskell-platform-2010.1.0.0 with ghc-6.12.2

* Wed Mar 24 2010 Jens Petersen <petersen@redhat.com> - 2010.1.0.0-1
- update to 2010.1.0.0 beta release
- update versions of alex, cgi, network, parallel, QuickCheck, HTTP
- new deepseq dep (#576482)

* Thu Jan 28 2010 Jens Petersen <petersen@redhat.com> - 2009.3.1.20100115-0.2
- add filelist for shared libs
- update devel post and postun

* Sat Jan 16 2010 Jens Petersen <petersen@redhat.com> - 2009.3.1.20100115-0.1
- update to darcs snapshot patched for ghc-6.12.1
- update to ghc-rpm-macros-0.5.1 and cabal2spec-0.21.1:
- drop doc and prof bcond
- use common_summary and common_description
- use ghc_lib_package and ghc_pkg_deps
- build shared library
- drop redundant buildroot and its install cleaning

* Mon Sep 28 2009 Jens Petersen <petersen@redhat.com> - 2009.2.0.2-3
- fix rpmlint warnings (bos, #523883)

* Mon Sep 28 2009 Jens Petersen <petersen@redhat.com> - 2009.2.0.2-2
- add all the buildrequires (#523883)
- create ghcpkgdir since metapackage
- nothing in bindir

* Thu Sep 17 2009 Jens Petersen <petersen@redhat.com> - 2009.2.0.2-1
- initial packaging for Fedora
