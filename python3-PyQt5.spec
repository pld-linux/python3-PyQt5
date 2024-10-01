#
# Conditional build:
%bcond_with	enginio		# Qt5Enginio support
%bcond_without	webkit		# Qt5WebKit support
%bcond_without	obsolete_py2	# whether to Obsolete python 2 packages

%define		module	PyQt5
# minimal required sip version
%define		sip_ver		6.8.6
# last qt version covered by these bindings (minimal required is currently 5.0.0)
# %define	qt_ver		%{version}
%define		qt_ver		5.15.0
%define		qtenginio_ver	1:1.6.0

Summary:	Python bindings for the Qt5 toolkit
Summary(pl.UTF-8):	Wiązania Pythona do toolkitu Qt5
Name:		python3-%{module}
Version:	5.15.11
Release:	2
License:	GPL v3
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/PyQt5/
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt5/PyQt5-%{version}.tar.gz
# Source0-md5:	51ff7c7ccec76a5de36db3ff88140eaf
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
BuildRequires:	Qt5Qml-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Quick3D-devel >= %{qt_ver}
BuildRequires:	Qt5RemoteObjects-devel >= %{qt_ver}
BuildRequires:	Qt5Sensors-devel >= %{qt_ver}
BuildRequires:	Qt5SerialPort-devel >= %{qt_ver}
BuildRequires:	Qt5Speech-devel >= %{qt_ver}
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
BuildRequires:	python3-PyQt-builder
BuildRequires:	python3-dbus >= 0.80
BuildRequires:	python3-devel >= 1:3.7
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-qmake >= %{qt_ver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	sip6 >= %{sip_ver}
Requires:	python3-dbus >= 0.80
Requires:	python3-libs >= 1:3.7
%if %{with obsolete_py2}
Obsoletes:	python-PyQt5 < 5.15.7-1
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyQt5 is a set of Python bindings for the Qt5 toolkit. The bindings
are implemented as a set of Python modules: Qt, QtBluetooth, QtCore,
QtDBus, QtDesigner, QtGui, QtHelp, QtLocation, QtMultimedia,
QtMultimediaWidgets, QtNetwork, QtNfc, QtOpenGL, QtPositioning,
QtPrintSupport, QtQml, QtQuick, QtQuickWidgets, QtSensors,
QtSerialPort, QtSql, QtSvg, QtTest, QtTextToSpeech, QtWebChannel,
QtWebSockets, QtX11Extras and QtXmlPatterns.

%description -l pl.UTF-8
PyQt5 to zbiór dowiązań do Qt5 dla Pythona. Dowiązania zostały
zaimplementowane jako moduły Pythona: Qt, QtBluetooth, QtCore, QtDBus,
QtDesigner, QtGui, QtHelp, QtLocation, QtMultimedia,
QtMultimediaWidgets, QtNetwork, QtNfc, QtOpenGL, QtPositioning,
QtPrintSupport, QtQml, QtQuick, QtQuickWidgets, QtSensors,
QtSerialPort, QtSql, QtSvg, QtTest, QtTextToSpeech, QtWebChannel,
QtWebSockets, QtX11Extras oraz QtXmlPatterns.

%package devel
Summary:	SIP files needed to build other bindings based on Qt5
Summary(pl.UTF-8):	Pliki SIP potrzebne do budowania innych wiązań opartych na Qt5
Group:		Development/Languages/Python
Requires:	sip6 >= %{sip_ver}
Obsoletes:	python3-PyQt5-sip-devel < 2:5
%if %{with obsolete_py2}
Obsoletes:	python-PyQt5-devel < 5.3.2-4
Obsoletes:	python-PyQt5-sip-devel < 2:5
Obsoletes:	sip-PyQt5 < 5.15.11-2
%else
# unfortunately boolean caps are not allowed for Obsoletes
#Obsoletes:	(sip-PyQt5 >= 5.15.6 with sip-PyQt5 < 5.15.11-2)
Obsoletes:	sip-PyQt5 >= 5.15.6
%endif

%description devel
SIP files needed to build other bindings for C++ classes that inherit
from any of the Qt5 classes (e.g. KDE or your own).

%description devel -l pl.UTF-8
Pliki SIP potrzebne do budowania innych wiązań do klas C++
dziedziczących z dowolnej klasy Qt5 (np. KDE lub własnych).

%package uic
Summary:	pyuic5 development tool for Python
Summary(pl.UTF-8):	Narzędzie programistyczne pyuic5 dla Pythona
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Xml >= %{qt_ver}
Obsoletes:	python-PyQt5-uic < 5.15.7-1

%description uic
pyuic5 development tool for Python.

%description uic -l pl.UTF-8
Narzędzie programistyczne pyuic5 dla Pythona.

%package devel-tools
Summary:	PyQt5 development tools
Summary(pl.UTF-8):	Narzędzia programistyczne PyQt5
Group:		Development/Tools
Requires:	python3-PyQt5 = %{version}-%{release}
Obsoletes:	python-PyQt5-devel-tools < 5.15.7-1

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
BuildArch:	noarch

%description examples
Examples code demonstrating how to use the Python bindings for Qt5.

%description examples -l pl.UTF-8
Przykładowy kod demonstrujący jak używać PyQt5.

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

%prep
%setup -q -n PyQt5-%{version}

grep -rl /usr/bin/env examples | xargs sed -i -e '1{
	s,^#!.*bin/env python$,#!%{__python3},
}'

%build
sip-build --build-dir build-py3 \
	--jobs %{__jobs} \
	--verbose \
	--confirm-license \
	--pep484-pyi \
	--qmake="%{_qt5_qmake}" \
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
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtTextToSpeech.abi3.so
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
%{py3_sitedir}/PyQt5-%{version}.dist-info

# annotations (-devel?)
%{?with_enginio:%{py3_sitedir}/PyQt5/Enginio.pyi}
%{py3_sitedir}/PyQt5/QtBluetooth.pyi
%{py3_sitedir}/PyQt5/QtCore.pyi
%{py3_sitedir}/PyQt5/QtDBus.pyi
%{py3_sitedir}/PyQt5/QtDesigner.pyi
%{py3_sitedir}/PyQt5/QtGui.pyi
%{py3_sitedir}/PyQt5/QtHelp.pyi
%{py3_sitedir}/PyQt5/QtLocation.pyi
%{py3_sitedir}/PyQt5/QtMultimedia.pyi
%{py3_sitedir}/PyQt5/QtMultimediaWidgets.pyi
%{py3_sitedir}/PyQt5/QtNetwork.pyi
%{py3_sitedir}/PyQt5/QtNfc.pyi
%{py3_sitedir}/PyQt5/QtOpenGL.pyi
%{py3_sitedir}/PyQt5/QtPositioning.pyi
%{py3_sitedir}/PyQt5/QtPrintSupport.pyi
%{py3_sitedir}/PyQt5/QtQml.pyi
%{py3_sitedir}/PyQt5/QtQuick.pyi
%{py3_sitedir}/PyQt5/QtQuick3D.pyi
%{py3_sitedir}/PyQt5/QtQuickWidgets.pyi
%{py3_sitedir}/PyQt5/QtRemoteObjects.pyi
%{py3_sitedir}/PyQt5/QtSensors.pyi
%{py3_sitedir}/PyQt5/QtSerialPort.pyi
%{py3_sitedir}/PyQt5/QtSql.pyi
%{py3_sitedir}/PyQt5/QtSvg.pyi
%{py3_sitedir}/PyQt5/QtTest.pyi
%{py3_sitedir}/PyQt5/QtTextToSpeech.pyi
%{py3_sitedir}/PyQt5/QtWebChannel.pyi
%if %{with webkit}
%{py3_sitedir}/PyQt5/QtWebKit.pyi
%{py3_sitedir}/PyQt5/QtWebKitWidgets.pyi
%endif
%{py3_sitedir}/PyQt5/QtWebSockets.pyi
%{py3_sitedir}/PyQt5/QtWidgets.pyi
%{py3_sitedir}/PyQt5/QtX11Extras.pyi
%{py3_sitedir}/PyQt5/QtXml.pyi
%{py3_sitedir}/PyQt5/QtXmlPatterns.pyi
%{py3_sitedir}/PyQt5/py.typed

%files devel
%defattr(644,root,root,755)
%{py3_sitedir}/PyQt5/bindings
%{py3_sitedir}/PyQt5/sip.pyi

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

%files -n Qt5Designer-plugin-pyqt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/libpyqt5.so
