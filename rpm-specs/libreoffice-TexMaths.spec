%global extname TexMaths

Name:           libreoffice-%{extname}
Version:        0.48.2
Release:        2%{?dist}
Summary:        A LaTex Equation Editor for LibreOffice

License:        GPLv2+
URL:            http://roland65.free.fr/texmaths/
Source0:        http://downloads.sourceforge.net/texmaths/%{extname}-%{version}.oxt

BuildRequires: libreoffice-sdk
# Needs the draw component
Requires: libreoffice-draw
# Needs at least writer or impress to be useful
Requires: libreoffice-writer
# We end up missing deps if we go with just /usr/bin/latex or similar
Requires: tex(latex)
Requires: /usr/bin/dvipng
Obsoletes: openoffice.org-ooolatex < 4.0.0-0.15

# We are actually not compiled
%global debug_package %{nil}

# The location of the installed extension.
%global loextdir %{_libdir}/libreoffice/share/extensions/%{extname}

# EL8 s390x is missing libreoffice-sdk
# EL8 aarch64 is missing dependencies for libreoffice-core:
#  https://bugzilla.redhat.com/show_bug.cgi?id=1849799
%if 0%{?el8}
ExcludeArch: aarch64 s390x
%endif

%description
TexMaths is a LaTeX equation editor for LibreOffice.  It is derived from
OOoLatex, originally developed by Geoffroy Piroux.

As its predecessor, TexMaths is a LibreOffice extension that allows you to
enter and edit LaTeX equations directly into LibreOffice documents.


%prep
%setup -q -c
# Fix FSF address
sed -i -e 's/59 Temple Place/51 Franklin Street/' -e 's/Suite 330/Fifth Floor/' \
  -e 's/MA  02111-1307/MA  02110-1301/' license.txt


%install
mkdir -p $RPM_BUILD_ROOT%{loextdir}
# remove binaries that are already included in latex2emf/libEMF
# copy the rest
cp -a * $RPM_BUILD_ROOT%{loextdir}
# remove documentation already in doc
rm $RPM_BUILD_ROOT%{loextdir}/{README,license.txt}


%files
%license license.txt
%doc README
%{loextdir}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.48.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 01 2020 Ian McInerney <ian.s.mcinerney@ieee.org> - 0.48.2-1
- Update to 0.48.2

* Mon Mar 30 2020 Ian McInerney <ian.s.mcinerney@ieee.org> - 0.48.1-1
- Update to 0.48.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 2019 Orion Poplawski <orion@nwra.com> - 0.48-1
- Update to 0.48

* Tue May 28 2019 Orion Poplawski <orion@nwra.com> - 0.47-1
- Update to 0.47

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.46.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Orion Poplawski <orion@nwra.com> - 0.46.1-1
- Update to 0.46.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 12 2016 Orion Poplawski <orion@cora.nwra.com> - 0.42-1
- Update to 0.42

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 30 2014 Orion Poplawski <orion@cora.nwra.com> - 0.41-1
- Update to 0.41

* Thu Oct 30 2014 Orion Poplawski <orion@cora.nwra.com> - 0.39-3
- Disable debuginfo generation

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 24 2014 Orion Poplawski <orion@cora.nwra.com> - 0.39-1
- Initial Fedora package.
