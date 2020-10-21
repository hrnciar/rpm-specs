# LibreOffice doesn't provide arch-independent extension directory, although
# Grammalecte extension is arch-independant. See also item 6 on
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LibreOfficeExtensions/
%global debug_package %{nil}

%global _description %{expand:Grammalecte is a grammar checker for the French language, derived from
Lightproof. Grammalecte helps writing a proper French, without distracting users
with false positives. This grammar checker follows the principle: the less false
positives, the better; if it cannot know with a good chance that a dubious
expression is wrong, it keeps silent.}
%global _description_fr %{expand:Grammalecte est un correcteur grammatical dédié à la langue française, dérivé de
Lightproof. Grammalecte essaie d'apporter une aide à l'écriture du français sans
parasiter l'attention des utilisateurs avec de fausses alertes. Ce correcteur
suit donc le principe suivant : le moins de « faux positifs » possible ; s'il
n'est pas possible de déterminer avec de fortes chances qu'une suite de mots
douteuse est erronée, le correcteur ne signalera rien.}

Name:           grammalecte
Version:        1.12.2
Release:        2%{?dist}
Summary:        French grammar checker
Summary(fr):    Correcteur grammatical dédié à la langue française

# Source code is GPLv3. Language resources in
# gc_lang/fr/oxt/Dictionnaires/dictionaries/ are:
# - MPLv2.0 for dictionaries (*.dic) and affix files (*.aff)
# - LGPLv2+ for French thesaurus (thes_fr.*) and hyphenation rules (*.tex)
# See ./gc_lang/fr/oxt/Dictionnaires/dictionaries/README*.txt
License:        GPLv3 and MPLv2.0 and LGPLv2+
URL:            https://grammalecte.net/
Source0:        %{name}-%{version}.tar.xz
# The source for this package was pulled from upstream's VCS. Use the
# following script to generate the tarball (fossil is required):
Source1:        %{name}-generate-tarball.sh
Source2:        libreoffice-%{name}.metainfo.xml

BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist bottle}
BuildRequires:  %{py3_dist setuptools}

%description
%{_description}

%description -l fr
%{_description_fr}


%package -n libreoffice-%{name}
Summary:        French grammar checker for LibreOffice Writer
Summary(fr):    Correcteur grammatical dédié à la langue française pour LibreOffice Writer
Requires:       %{py3_dist grammalecte-fr}
Requires:       libreoffice-langpack-fr
Requires:       libreoffice-pyuno
Requires:       libreoffice-writer

%description -n libreoffice-%{name}
%{_description}

This package provides the LibreOffice Writer extension.

%description -l fr -n libreoffice-%{name}
%{_description_fr}

Ce paquet fournit l'extension pour LibreOffice Writer.


%package -n python3-%{name}
Summary:        French grammar checker
Summary(fr):    Correcteur grammatical dédié à la langue française
Requires:       %{py3_dist bottle}
Provides:       %{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}
BuildArch:      noarch

%description -n python3-%{name}
%{_description}

This package provides the command line interface, along with a server and a
Python library.

%description -l fr -n python3-%{name}
%{_description_fr}

Ce paquet fournit l'interface en ligne de commande ainsi qu'un serveur et une
bibliothèque Python.


%prep
%autosetup

# Use system bottle library for build
ln -sf %{python3_sitelib}/bottle.py 3rd/


%build
# Build LibreOffice extension and Python module ZIP
%{__python3} make.py -b -d fr

# Build Python module
mkdir python/
unzip _build/Grammalecte-fr-v%{version}.zip -d python/
pushd python/
rm -rf *.egg-info
%py3_build
popd


%install
# Install LibreOffice extension
install -dm 0755 $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/extensions/%{name}/
unzip _build/Grammalecte-fr-v%{version}.oxt \
    -d $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/extensions/%{name}/ \
    -x "pythonpath/%{name}-cli.py" \
    -x "pythonpath/%{name}/*"
# Fix permissions
find $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/extensions/%{name}/ -type f | xargs chmod 0644

# Install Python module
pushd python/
%py3_install
popd

# Unbundle bottle library
ln -sf %{python3_sitelib}/bottle.py $RPM_BUILD_ROOT%{python3_sitelib}/%{name}/bottle.py

# Avoid code duplication accross subpackages
ln -s %{_bindir}/%{name}-cli.py $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/extensions/%{name}/pythonpath/
ln -s %{python3_sitelib}/%{name} $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/extensions/%{name}/pythonpath/

install -Dpm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml


%check
%{__python3} ./make.py fr -t

pushd python/
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitelib}/ %{__python3} setup.py test
popd

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml


%files -n libreoffice-%{name}
%doc README.txt
%license LICENSE.txt LICENSE.fr.txt ./gc_lang/fr/oxt/Dictionnaires/dictionaries/README*.txt
%{_libdir}/libreoffice/share/extensions/%{name}/
%{_metainfodir}/%{name}.appdata.xml


%files -n python3-%{name}
%doc python/README.txt
%license python/{LICENSE.txt,LICENSE.fr.txt}
%{_bindir}/%{name}-cli.py
%{_bindir}/%{name}-server.py
%{python3_sitelib}/%{name}/
%{python3_sitelib}/Grammalecte_fr-*.egg-info/


%changelog
* Tue Oct 06 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.12.2-2
- Add BuildRequires on python3-setuptools

* Wed Sep 02 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.12.2-1
- Initial RPM release
