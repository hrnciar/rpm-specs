%global packname rmarkdown
%global packver  2.4
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((dygraphs)\\)

# Recursive dependencies.
%global with_suggests 0

Name:             R-%{packname}
Version:          2.4
Release:          1%{?dist}
Summary:          Dynamic Documents for R

# Main is GPLv3; see bundled Provides below for others.
License:          GPLv3 and ASL 2.0 and BSD and MIT and W3C
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Remove-unused-minified-ioslides-files.patch
Patch0002:        0002-Unbundle-fonts-in-ioslides.patch
Patch0004:        0004-Add-original-non-minified-Bootswatch-themes.patch
Patch0005:        0005-Unbundle-fonts-from-bootstrap.patch
Patch0006:        0006-Add-source-for-code-prettify.patch
Patch0007:        0007-Skip-shiny-tests.patch
%if 0%{?fedora} >= 33
Patch0008:        0008-handle-updated-Raleway-fonts-in-f33.patch
%endif

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-tools, R-utils, R-knitr >= 1.22, R-yaml >= 2.1.19, R-htmltools >= 0.3.5, R-evaluate >= 0.13, R-jsonlite, R-mime, R-tinytex >= 0.11, R-xfun, R-methods, R-stringr >= 1.2.0
# Suggests:  R-shiny >= 0.11, R-tufte, R-testthat, R-digest, R-dygraphs, R-tibble, R-fs, R-rsconnect
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         pandoc >= 1.12.3
Requires:         pandoc-citeproc

BuildRequires:    git-core
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    pandoc >= 1.12.3
BuildRequires:    pandoc-citeproc
BuildRequires:    golang-github-tdewolff-minify
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-knitr >= 1.22
BuildRequires:    R-yaml >= 2.1.19
BuildRequires:    R-htmltools >= 0.3.5
BuildRequires:    R-evaluate >= 0.13
BuildRequires:    R-jsonlite
BuildRequires:    R-mime
BuildRequires:    R-tinytex >= 0.11
BuildRequires:    R-xfun
BuildRequires:    R-methods
BuildRequires:    R-stringr >= 1.2.0
BuildRequires:    R-testthat
BuildRequires:    R-digest
BuildRequires:    R-rsconnect
%if %{with_suggests}
BuildRequires:    R-shiny >= 0.11
BuildRequires:    R-tufte
BuildRequires:    R-dygraphs
BuildRequires:    R-tibble
BuildRequires:    R-fs
%endif

#BuildRequires:    fontawesome-fonts = 4.7.0
#BuildRequires:    fontawesome-fonts-web = 4.7.0
#Recommends:       fontawesome-fonts = 4.7.0
#Recommends:       fontawesome-fonts-web = 4.7.0
Provides:         bundled(fontawesome-fonts) = 5.1.0
Provides:         bundled(fontawesome-fonts-web) = 5.1.0

# These are not all packaged, but should *probably* be the names if they are.

# MIT; inst/rmd/h/bootstrap/
# https://github.com/twbs/bootstrap/releases/tag/v3.3.5
Provides:         bundled(xstatic-bootstrap-common) = 3.3.5
BuildRequires:    adobe-source-sans-pro-fonts
Recommends:       adobe-source-sans-pro-fonts
BuildRequires:    glyphicons-halflings-fonts
Recommends:       glyphicons-halflings-fonts
BuildRequires:    glyphography-newscycle-fonts
Recommends:       glyphography-newscycle-fonts
BuildRequires:    google-roboto-fonts
Recommends:       google-roboto-fonts
BuildRequires:    impallari-raleway-fonts
Recommends:       impallari-raleway-fonts
BuildRequires:    lato-fonts
Recommends:       lato-fonts

# BSD; inst/rmd/h/highlightjs/ (unbundled)
#BuildRequires:    js-highlight
#Requires:         js-highlight
# Currently broken in Fedora
Provides:         bundled(js-highlight) = 9.12.0

# MIT; inst/rmd/h/ionicons/
# http://ionicons.com/
Provides:         bundled(ionicons-fonts) = 2.0.1

# MIT; inst/rmd/h/jquery/
Provides:         bundled(js-jquery1) = 1.12.4

# MIT; inst/rmd/h/jqueryui (outdated in Fedora)
Provides:         bundled(xstatic-jquery-ui-common) = 1.11.4

# MIT; inst/rmd/h/navigation-1.1/tabsets.js
# https://github.com/aidanlister/jquery-stickytabs (partially)
Provides:         bundled(js-jquery-stickytabs) = 1.2.4

# MIT; inst/rmd/h/tocify/
# http://gregfranko.com/jquery.tocify.js/
Provides:         bundled(js-jquery-tocify) = 1.9.1

# ASL 2.0; inst/rmd/ioslides/ioslides-13.5.1/
Provides:         bundled(js-ioslides) = 13.5.1
# MIT; inst/rmd/ioslides/ioslides-13.5.1/js/hammer.js
# https://hammerjs.github.io/
Provides:         bundled(js-hammer) = 0.4
# MIT & BSD; inst/rmd/ioslides/ioslides-13.5.1/js/modernizr.custom.45394.js
# https://modernizr.com/
Provides:         bundled(js-modernizr) = 2.5.3
# ASL 2.0; inst/rmd/ioslides/ioslides-13.5.1/js/prettify/
# https://github.com/google/code-prettify
Provides:         bundled(js-code-prettify) = 20130304
BuildRequires:    open-sans-fonts
Recommends:       open-sans-fonts
BuildRequires:    adobe-source-code-pro-fonts
Recommends:       adobe-source-code-pro-fonts

# W3C; inst/rmd/slidy/Slidy2/
# https://www.w3.org/Talks/Tools/Slidy2/
Provides:         bundled(js-slidy) = 2

%description
Convert R Markdown documents into a variety of formats.


%prep
%setup -q -c -n %{packname}
%autosetup -D -T -n %{packname}/%{packname} -S git

# Must be removed: https://bugzilla.redhat.com/show_bug.cgi?id=961642#c4
rm inst/rmd/h/bootstrap/css/fonts/Ubuntu.ttf

# Fix executable bits
chmod -x inst/rmd/h/ionicons/{LICENSE,css/*.css,fonts/*.ttf}
chmod -x inst/rmd/ioslides/ioslides-13.5.1/js/hammer.js

# Fix fonts using new paths.
%if 0%{?fedora} >= 33
for f in Bold It Light Regular; do
    ln -sf /usr/share/fonts/adobe-source-sans-pro-fonts/SourceSans3-${f}.otf inst/rmd/h/bootstrap/css/fonts/SourceSansPro-${f}.otf
done
%endif

# This does nothing but reset the -n path.
%setup -q -D -T -n %{packname}


%build
gominify --type css \
    < %{packname}/inst/rmd/h/ionicons/css/ionicons.css \
    > %{packname}/inst/rmd/h/ionicons/css/ionicons.min.css
pushd %{packname}/inst/rmd/h/bootstrap/css/
for file in bootstrap bootstrap-theme cerulean cosmo darkly flatly journal lumen paper readable sandstone simplex spacelab united yeti; do
    gominify --type css < ${file}.css > ${file}.min.css
done
popd


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
pushd %{buildroot}%{rlibdir}/%{packname}
# Remove bundled fonts in ioslides.
rm rmd/ioslides/ioslides-13.5.1/fonts/OpenSans*.ttf
for f in OpenSans-Regular OpenSans-Italic OpenSans-Semibold OpenSans-SemiboldItalic; do
    ln -s /usr/share/fonts/open-sans/${f}.ttf rmd/ioslides/ioslides-13.5.1/fonts/${f}.ttf
done
ln -sf /usr/share/fonts/adobe-source-code-pro/SourceCodePro-Regular.otf rmd/ioslides/ioslides-13.5.1/fonts/SourceCodePro-Regular.otf
# Remove bundled FontAwesome. (too new to remove)
#rm -r rmd/h/fontawesome/*
#ln -s /usr/share/font-awesome-web/css rmd/h/fontawesome/css
#ln -s /usr/share/fonts/fontawesome rmd/h/fontawesome/fonts
# Remove bundled fonts from bootstrap.
ln -sf /usr/share/fonts/lato/Lato-Regular.ttf rmd/h/bootstrap/css/fonts/Lato.ttf
ln -sf /usr/share/fonts/lato/Lato-Bold.ttf rmd/h/bootstrap/css/fonts/LatoBold.ttf
ln -sf /usr/share/fonts/lato/Lato-Italic.ttf rmd/h/bootstrap/css/fonts/LatoItalic.ttf
ln -sf /usr/share/fonts/glyphography-newscycle-fonts/newscycle-regular.ttf rmd/h/bootstrap/css/fonts/NewsCycle.ttf
ln -sf /usr/share/fonts/glyphography-newscycle-fonts/newscycle-bold.ttf rmd/h/bootstrap/css/fonts/NewsCycleBold.ttf
ln -sf /usr/share/fonts/open-sans/OpenSans-Regular.ttf rmd/h/bootstrap/css/fonts/OpenSans.ttf
for f in Bold BoldItalic Italic Light LightItalic; do
    ln -sf /usr/share/fonts/open-sans/OpenSans-${f}.ttf rmd/h/bootstrap/css/fonts/OpenSans${f}.ttf
done
for f in Regular Bold; do
%if 0%{?fedora} >= 33
    ln -sf /usr/share/fonts/impallari-raleway-fonts/Raleway-${f}.ttf rmd/h/bootstrap/css/fonts/Raleway-${f}.ttf
%else
    ln -sf /usr/share/fonts/impallari-raleway/Raleway-${f}.otf rmd/h/bootstrap/css/fonts/Raleway-${f}.otf
%endif
done
ln -sf /usr/share/fonts/google-roboto/Roboto-Regular.ttf rmd/h/bootstrap/css/fonts/Roboto.ttf
for f in Light Medium Bold; do
    ln -sf /usr/share/fonts/google-roboto/Roboto-${f}.ttf rmd/h/bootstrap/css/fonts/Roboto${f}.ttf
done
for f in Bold It Light Regular; do
%if 0%{?fedora} >= 33
    ln -sf /usr/share/fonts/adobe-source-sans-pro-fonts/SourceSans3-${f}.otf rmd/h/bootstrap/css/fonts/SourceSansPro-${f}.otf
%else
    ln -sf /usr/share/fonts/source-sans-pro/SourceSansPro-${f}.otf rmd/h/bootstrap/css/fonts/SourceSansPro-${f}.otf
%endif
done
ln -sf /usr/share/fonts/glyphicons-halflings/glyphicons-halflings-regular.ttf rmd/h/bootstrap/fonts/glyphicons-halflings-regular.ttf
popd


%check
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/COPYING
%license %{rlibdir}/%{packname}/NOTICE
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/rmarkdown
%dir %{rlibdir}/%{packname}/rmd
%{rlibdir}/%{packname}/rmd/fragment
%dir %{rlibdir}/%{packname}/rmd/h
%{rlibdir}/%{packname}/rmd/h/_navbar.html
%{rlibdir}/%{packname}/rmd/h/accessibility
%{rlibdir}/%{packname}/rmd/h/default.html
%{rlibdir}/%{packname}/rmd/h/bootstrap
%{rlibdir}/%{packname}/rmd/h/fontawesome
%{rlibdir}/%{packname}/rmd/h/highlightjs
%{rlibdir}/%{packname}/rmd/h/ionicons
%{rlibdir}/%{packname}/rmd/h/jquery
%{rlibdir}/%{packname}/rmd/h/jquery-AUTHORS.txt
%{rlibdir}/%{packname}/rmd/h/jqueryui
%{rlibdir}/%{packname}/rmd/h/jqueryui-AUTHORS.txt
%{rlibdir}/%{packname}/rmd/h/navigation-1.1
%{rlibdir}/%{packname}/rmd/h/pagedtable-1.1
%{rlibdir}/%{packname}/rmd/h/pandoc
%{rlibdir}/%{packname}/rmd/h/rmarkdown
%{rlibdir}/%{packname}/rmd/h/rsiframe-1.1
%{rlibdir}/%{packname}/rmd/h/tocify
%{rlibdir}/%{packname}/rmd/ioslides
%{rlibdir}/%{packname}/rmd/latex
%{rlibdir}/%{packname}/rmd/site
%{rlibdir}/%{packname}/rmd/slidy
%{rlibdir}/%{packname}/rstudio


%changelog
* Wed Sep 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4-1
- Update to latest version (#1884046)
- Fix Rawhide/f33 font unbundling for Adobe SourceSans
- Unbundle NewsCycle font

* Sat Aug 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3-1
- Update to latest version
- Switch minification from ycssmin to gominify
- Fix Rawhide font unbundling
- Re-enable tests
- Re-bundle jquery; it's retired in Rawhide

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 2.2-1
- update to 2.2
- move R-fs within the with_suggests conditional to simplify build
- rebuild for R 4
- handle updated Raleway fonts in f33+
- disable check (hopefully temporarily)

* Wed Mar 04 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.18-2
- Re-bundle highlightjs, which is broken in Fedora

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0-1
- Update to latest version

* Wed Nov 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.18-1
- Update to latest version

* Wed Nov 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.17-1
- Update to latest version

* Wed Oct 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16-1
- Update to latest version

* Sun Aug 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.15-1
- Update to latest version

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.14-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.13-4
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.13-2
- Switch to git autosetup instead of manual patches
- Update bootstrap unbundling and re-compress CSS

* Wed May 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.13-1
- Update to latest version

* Thu Mar 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12-1
- Update to latest version

* Mon Mar 04 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.11-1
- Update to latest version
- Fix unbundling of highlightjs
- Move dependencies from Suggests to Recommends to work better out-of-the-box

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10-4
- Fix unbundling of fonts

* Sat Sep 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10-3
- Add missing jquery Requires

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10-1
- Update to latest version

* Sun Apr 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.9-1
- initial package for Fedora
