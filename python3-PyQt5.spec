#
# Conditional build:
%bcond_with	enginio		# Qt5Enginio support
%bcond_without	webkit		# Qt5WebKit support

%define		module	PyQt5
# minimal required sip version
%define		sip_ver		6.4
# last qt version covered by these bindings (minimal required is currently 5.0.0)
# %define	qt_ver		%{version}
%define		qt_ver		5.15.0
%define		qtenginio_ver	1:1.6.0

Summary:	Python bindings for the Qt5 toolkit
Summary(pl.UTF-8):	Wiązania Pythona do toolkitu Qt5
Name:		python3-%{module}
Version:	5.15.7
Release:	1
License:	GPL v3
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/PyQt5/
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt5/PyQt5-%{version}.tar.gz
# Source0-md5:	ae2c68e38b9b36fdf5f932419353a2b3
URL:		https://riverbankcomputing.com/software/pyqt/intro
# most of BR comes from configure.py
BuildRequires:	Qt5Bluetooth-devel >= %{qt_ver}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Designer-devel >= %{qt_ver}
%{?with_enginio:BuildRequires:	Qt5Enginio-devel >= %{qtenginio_ver}}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Help-devel >= %{qt_ver}
BuildRequires:	Qt5Location-devel >= %{qt_ver}
BuildRequires:	Qt5Multimedia-devel >= %{qt_ver}
BuildRequires:	Qt5MultimediaWidgets-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5Nfc-devel >= %{qt_ver}
BuildRequires:	Qt5OpenGL-devel >= %{qt_ver}
BuildRequires:	Qt5Positioning-devel >= %{qt_ver}
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5RemoteObjects-devel >= %{qt_ver}
BuildRequires:	Qt5Qml-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Quick3D-devel >= %{qt_ver}
BuildRequires:	Qt5Sensors-devel >= %{qt_ver}
BuildRequires:	Qt5SerialPort-devel >= %{qt_ver}
BuildRequires:	Qt5Sql-devel >= %{qt_ver}
BuildRequires:	Qt5Svg-devel >= %{qt_ver}
BuildRequires:	Qt5Test-devel >= %{qt_ver}
BuildRequires:	Qt5UiTools-devel >= %{qt_ver}
BuildRequires:	Qt5WebChannel-devel >= %{qt_ver}
%{?with_webkit:BuildRequires:	Qt5WebKit-devel >= %{qt_ver}}
BuildRequires:	Qt5WebSockets-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt_ver}
BuildRequires:	Qt5Xml-devel >= %{qt_ver}
BuildRequires:	Qt5XmlPatterns-devel >= %{qt_ver}
BuildRequires:	dbus-devel >= 1
BuildRequires:	pkgconfig
BuildRequires:	python-dbus-devel >= 0.80
BuildRequires:	python3-dbus >= 0.80
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-qmake >= %{qt_ver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sip6 >= %{sip_ver}
Requires:	python3-dbus >= 0.80
Requires:	python3-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyQt5 is a set of Python bindings for the Qt5 toolkit. The bindings
are implemented as a set of Python modules: Qt, QtBluetooth, QtCore,
QtDBus, QtDesigner, QtGui, QtHelp, QtLocation, QtMultimedia,
QtMultimediaWidgets, QtNetwork, QtNfc, QtOpenGL, QtPositioning,
QtPrintSupport, QtQml, QtQuick, QtQuickWidgets, QtSensors,
QtSerialPort, QtSql, QtSvg, QtTest, QtWebChannel,
QtWebSockets, QtX11Extras and QtXmlPatterns.

%description -l pl.UTF-8
PyQt5 to zbiór dowiązań do Qt5 dla Pythona. Dowiązania zostały
zaimplementowane jako moduły Pythona: Qt, QtBluetooth, QtCore, QtDBus,
QtDesigner, QtGui, QtHelp, QtLocation, QtMultimedia,
QtMultimediaWidgets, QtNetwork, QtNfc, QtOpenGL, QtPositioning,
QtPrintSupport, QtQml, QtQuick, QtQuickWidgets, QtSensors,
QtSerialPort, QtSql, QtSvg, QtTest, QtWebChannel,
QtWebSockets, QtX11Extras oraz QtXmlPatterns.

%package uic
Summary:	pyuic5 development tool for Python
Summary(pl.UTF-8):	Narzędzie programistyczne pyuic5 dla Pythona
Group:		Development/Tools
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Xml >= %{qt_ver}
Requires:	%{name} = %{version}-%{release}

%description uic
pyuic5 development tool for Python.

%description uic -l pl.UTF-8
Narzędzie programistyczne pyuic5 dla Pythona.

%package devel-tools
Summary:	PyQt5 development tools
Summary(pl.UTF-8):	Narzędzia programistyczne PyQt5
Group:		Development/Tools
Requires:	python3-PyQt5 = %{version}-%{release}

%description devel-tools
PyQt5 development tools: pylupdate5, pyrcc5.

Note: this package doesn't depend on Python version.

%description devel-tools -l pl.UTF-8
Narzędzia programistyczne PyQt5: pylupdate5, pyrcc5.

Uwaga: ten pakiet nie jest zależny od wersji Pythona.

%package examples
Summary:	Examples for PyQt5
Summary(pl.UTF-8):	Przykłady do PyQt5
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples code demonstrating how to use the Python bindings for Qt5.

%description examples -l pl.UTF-8
Przykładowy kod demonstrujący jak używać PyQt5.

%package -n sip-PyQt5
Summary:	SIP files needed to build other bindings based on Qt5
Summary(pl.UTF-8):	Pliki SIP potrzebne do budowania innych wiązań opartych na Qt5
Group:		Development/Languages/Python
Requires:	sip6 >= %{sip_ver}
Obsoletes:	python-PyQt5-devel < 5.3.2-4

%description -n sip-PyQt5
SIP files needed to build other bindings for C++ classes that inherit
from any of the Qt5 classes (e.g. KDE or your own).

%description -n sip-PyQt5 -l pl.UTF-8
Pliki SIP potrzebne do budowania innych wiązań do klas C++
dziedziczących z dowolnej klasy Qt5 (np. KDE lub własnych).

%package -n Qt5Designer-plugin-pyqt5
Summary:	Qt5 Designer plugin for Python plugins with widgets
Summary(pl.UTF-8):	Wtyczka Qt5 Designera dla wtyczek Pythona zawierających widgety
Requires:	python3-PyQt5 = %{version}-%{release}

%description -n Qt5Designer-plugin-pyqt5
This is the Qt5 Designer plugin that collects all the Python plugins
it can find as a widget collection to Designer.

%description -n Qt5Designer-plugin-pyqt5 -l pl.UTF-8
Ten pakiet zawiera wtyczkę Qt5 Designera zbierającą wszystkie wtyczki
Pythona, które jest w stanie znaleźć, jako zestaw widgetów dla
Designera.

%package -n qscintilla2-%{module}-api
Summary:	PyQt5 API file for QScintilla
Summary(pl.UTF-8):	Plik API PyQt5 dla QScintilli
Group:		Libraries/Python
Requires:	qscintilla2-qt5 >= 2.2-2

%description -n qscintilla2-%{module}-api
PyQt5 API file can be used by the QScintilla editor component to
enable the use of auto-completion and call tips when editing PyQt5
code.

%description -n qscintilla2-%{module}-api -l pl.UTF-8
Plik API PyQt5 może być używany przez komponent edytora QScintilla aby
umożliwić automatyczne dopełnianie i podpowiedzi przy modyfikowaniu
kodu wykorzystującego PyQt5.

%prep
%setup -q -n PyQt5-%{version}

grep -rl /usr/bin/env examples | xargs sed -i -e '1{
	s,^#!.*bin/env python$,#!%{__python3},
}'

%build
sip-build --build-dir build-py3 \
	--verbose \
	--confirm-license \
	--qmake="%{_bindir}/qmake-qt5" \
	--scripts-dir=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} -C build-py3 install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}

cp -R examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/plugins/PyQt5
%attr(755,root,root) %{_libdir}/qt5/plugins/PyQt5/libpyqt5qmlplugin.so
%dir %{py3_sitedir}/PyQt5
%attr(755,root,root) %{py3_sitedir}/PyQt5/pylupdate.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/pyrcc.abi3.so
%{?with_enginio:%attr(755,root,root) %{py3_sitedir}/PyQt5/Enginio.abi3.so}
%attr(755,root,root) %{py3_sitedir}/PyQt5/Qt.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtBluetooth.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtCore.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtDBus.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtDesigner.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtGui.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtHelp.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtLocation.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtMultimedia.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtMultimediaWidgets.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtNetwork.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtNfc.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtOpenGL.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtPositioning.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtPrintSupport.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtQml.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtQuick.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtQuick3D.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtQuickWidgets.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtRemoteObjects.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtSensors.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtSerialPort.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtSql.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtSvg.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtTest.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebChannel.abi3.so
%if %{with webkit}
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebKit.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebKitWidgets.abi3.so
%endif
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebSockets.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWidgets.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtX11Extras.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtXml.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtXmlPatterns.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/_QOpenGLFunctions_2_0.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/_QOpenGLFunctions_2_1.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/_QOpenGLFunctions_4_1_Core.abi3.so
%attr(755,root,root) %{py3_sitedir}/dbus/mainloop/pyqt5.abi3.so
%{py3_sitedir}/PyQt5/__init__.py
%{py3_sitedir}/PyQt5/pylupdate_main.py
%{py3_sitedir}/PyQt5/pyrcc_main.py
%{py3_sitedir}/PyQt5/__pycache__

%files uic
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pyuic5
%{py3_sitedir}/PyQt5/uic

%files devel-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pylupdate5
%attr(755,root,root) %{_bindir}/pyrcc5

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n sip-PyQt5
%defattr(644,root,root,755)
%{py3_sitedir}/PyQt5/bindings

%files -n Qt5Designer-plugin-pyqt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/libpyqt5.so

%files -n qscintilla2-%{module}-api
%defattr(644,root,root,755)
#%{_datadir}/qt5/qsci/api/python/PyQt5.api
